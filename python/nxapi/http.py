#!/usr/bin/env python2.7

# Copyright 2015 Cisco Systems, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

''' HTTP API of Nexus (NX). 

    @author: Ken Jarrad (kjarrad@cisco.com)
'''

from __future__ import print_function as _print_function
from requests import post, get, request, Session
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException
from logging import log, WARN as DEFAULT_LOG_LEVEL
from json import dumps
from collections import namedtuple
from itertools import chain
from tabulate import tabulate

_ins_api_version = '1.2'

# Name of cookie (in HTTP request and response).
_nexus_authentication_cookie_name = 'nxapi_auth'

def device_url(scheme='http', hostname='localhost', port=80, username=None, password=None):
    url = "%s://%s" % (scheme, hostname)
    if not (scheme, port) in [('http', 80), ('https', 443)]:
        url += ':' + str(port)
    return url

def session_device_url(session):
    return session.cookies['device-url']

def session_command_url(session):
    return session.cookies['command-url']

def connect(scheme='http', hostname='172.16.1.73', port=80, username='cisco', password='cisco'):
    """ Create new Session in _session_cache """
    session = Session()
    session.auth = (username, password)
    url = device_url(scheme, hostname, port)
    session.cookies['device-url'] = url
    session.cookies['command-url'] = url + '/ins'
    response = session.get(url)
    response.raise_for_status()
    assert _nexus_authentication_cookie_name in response.cookies
    return session

def disconnect(session):
    """ Create new Session in _session_cache """
    session.close()

def _json_rpc_request_payload(command='show version', sequence=1):
    return {
        "jsonrpc": "2.0",
        "method": "cli_schema",
        "params": {
            "cmd": command,
            "version": 1.2
        },
        "id": sequence
    }
                          

def json_rpc(session, commands=('show version', 'show route-map'), command_type='cli'):
    request_payload = []
    if isinstance(commands, (tuple, list)):
        if len(commands) > 1:
            for seq, command in enumerate(commands, start=1):
                request_payload.append(_json_rpc_request_payload(command, seq))
        elif len(commands) == 1:
            request_payload.append(_json_rpc_request_payload(commands[0]))
        else:
            assert len(commands) >= 1, 'Expected one or more commands, got zero.'
    else:
        request_payload.append(_json_rpc_request_payload(commands))
    request_payload = dumps(request_payload, indent=2)
    response = session.post(
            url=session_command_url(session),
            data=request_payload,
            headers={
                'Content-type' : 'application/json-rpc',
                'Accept' : 'application/json'
            }
        )
    #print('status code', response.status_code)
    response.raise_for_status()
    assert response.headers['Content-type'].endswith('/json-rpc')
    response_json = response.json()
    if isinstance(response_json,list):
        return {response_element['id'] : response_element['result'] for response_element in response_json}
    else:
        return {response_json['id'] : response_json['result']}

def cli(session, commands=('show version', 'show route-map'), command_type='cli_show', chunk=False):
    if isinstance(commands, (tuple, list)):
        command_text = ' ;'.join(commands)
    else:
        command_text = str(commands)
    request_payload = {
      "ins_api": {
        "version": str(_ins_api_version),
        "type": command_type,
        "chunk": str(int(chunk)),
        "sid": str(id(session)),
        "input": command_text,
        "output_format": "json"
      }
    }
    request_payload = dumps(request_payload, indent=2)
    response = session.post(
            url=session.cookies['command-url'],
            data=request_payload,
            headers={'Accept':'application/json'}
        )
    #print('status code', response.status_code)
    response.raise_for_status()
    assert response.headers['Content-type'].endswith('/json')
    response_data = response.json()
    return response_data

def cli_show(session, commands=('show version', 'show route-map'), chunk=False):
    response_data = cli(session=session, commands=commands, command_type='cli_show', chunk=chunk)
    command_responses = response_data['ins_api']['outputs']['output']
    if isinstance(command_responses, list):
        return {output['input'] : _command_body(output) for output in command_responses}
    else:
        assert isinstance(command_responses, dict)
        return {command_responses['input'] : _command_body(command_responses)}
#          print('body=',dumps(body,indent=2))

def _split_schema_field_info(schema_field_info):
    """
    Split one input string into a tuple of (type,description),
    where both 'type' and 'description' are type string.
    
    The delimiter is presumed to be '|'.
    """
    (field_type, field_description) = \
            tuple(schema_field_info.split('|')) if '|' in schema_field_info \
            else (schema_field_info, None) if len(schema_field_info) != 0 \
            else (None, None)
    return (
        field_type if field_type and len(field_type) != 0 else None, 
        field_description if field_description and len(field_description) != 0 else None
    )

def _unpack_schema_fields(schema_table):
    return {field_name:_split_schema_field_info(field_info) for (field_name,field_info) in schema_table.items()}
                          
def cli_schema(session, commands=('show version', 'show ip interface brief')):
    response_table = json_rpc(session=session, commands=commands, command_type='cli_schema')
    return {response['cmd'] : (response['syntax'], _unpack_schema_fields(response['doc']))
            for response in response_table.values()}
    
def print_command_schema(schema_table):
    for (command,(syntax,field_table)) in schema_table.items():
        print()
        print(tabulate([(command,syntax)],headers=('command','syntax')))
        print()
        alist=[(field_name,field_info[0],field_info[1]) for (field_name,field_info) in field_table.items()]
        print('Command Schema Fields:')
        print(tabulate(alist,headers=('name','type','description')))
    
def _command_body(command_output):
    """ Check the output of a command for errors.
    
    Input Parameters:
        command_output -    
            A dict of fields received in response to a command.
    
    Returns:
        The body of the output of a command.
        
    Raises:
        Error if command output contains an error message. 
    """
#     print('body=',dumps(body,indent=2))
    return command_output['body'] if 'body' in command_output else _command_raise_error(command_output)

def _command_raise_error(command_output):
    print('command_output', command_output)
    message = ', '.join(['%s="%s"' % (k, v) for (k, v) in command_output.items()])
    raise ValueError(message)

def _namedtuple_factory(typename, field_names):
    """ Find or create a namedtuple class as specified.
    
    This function does not yet find existing named-tuples.
    It creates a new class every time.
    Add @lru_cache decorator to achieve this.
    Also this will be thread-safe, which a simple dict would not.
    """
    return namedtuple(typename, field_names)
    
def _command_namedtuple(command_input, command_output):
    field_names = [field for field in command_output]
#     print(field_names)
#     field_names = [field.replace('-','_') for field in command_output]
    print(field_names)
    tuple_name = command_input.replace('-', '_').replace(' ', '_')
    print(tuple_name)
    nt = namedtuple(typename=tuple_name, field_names=field_names)
    print('id(nt)', id(nt), nt)
    if field_names:
        o = nt(**command_output)
    else:
        o = nt()
    print(o)
    return o
    
def main():
    session = connect()
    executed_commands = cli_show(session)
    # print(dumps(executed_commands,indent=2))
    for (k, v) in executed_commands.items():
        print(_command_namedtuple(k, v))
        print(_command_namedtuple(k, v))
        
    tu = _command_namedtuple(k, v)
    m = tu.memory
    nm = tu.not_memory
    print('memory', tu.memory)
    kicker = tu.kick_file_name
    print('complete kick', kicker)
        
    print(dumps(cli_show(session, 'show ip interface mgmt 0'), indent=2))
    for (k, v) in cli_show(session, 'show ip int mgmt 0').items():
        print(_command_namedtuple(k, v))
    
    # print(dumps(cli_show(session,'show cli list'),indent=2))
    
    # ken, use list of tuple(cmd/,output) not map{cmd:output} due to ordering of cmds and repeat of cmds
    
    # print(dir(session))
    # print(session.__dict__)
    # print(dir(session.adapters['http://']))
    # print(session.adapters['http://'].__dict__)
    # print(session.cookies['command-url'])
    
    
    # help(request)
    # for i in xrange(1, 13):
    #     nexus_authentication_token()
    #     for c in _session.cookies:
    #         print(c)
    #         print(dir(c))
    #         print('port', c.port)
    #         print('comment', c.comment)
    #         print('discard', c.discard)
    #         print('comment_url', c.comment_url)
    #         print('expires', c.expires)
    #         print('is_expired', c.is_expired())
    #         print('name', c.name)
    #         print('path', c.path)
    #         print('path_specified', c.path_specified)
    #         print('secure', c.secure)
    #         print('value', c.value)
    #         print('version', c.version)
    
    #     for field in dir(c):
    #         print(field, c.__dir__[field])
    # print(_nexus_authentication_cookie_jar[_nexus_authentication_cookie_name])
