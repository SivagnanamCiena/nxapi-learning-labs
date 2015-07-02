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

"""
Demonstrate how to obtain routing information of one network device.
"""
from __future__ import print_function
from inspect import cleandoc
from logging import log, WARN
from nxapi.http import cli_show, connect, disconnect, cli_schema, print_command_schema, session_device_url
from nxapi.context import sys_exit, EX_OK, EX_TEMPFAIL
from nxapi.render import print_table
from example import inventory_config
from collections import OrderedDict

command = 'sh routing'

def demonstrate(session):
    """ Execute a command, print the output, return True if successful. """
    response = cli_show(session, command)
    for c in response:
        print('Output for command:', c)
        output = response[c]

        table_vrf = output['TABLE_vrf']
        display_table = []
        rows_vrf = table_vrf['ROW_vrf']
        if not isinstance(rows_vrf, list):
            rows_vrf = [rows_vrf]
        for row_vrf in rows_vrf:
            display_vrf = OrderedDict()
            keys = [k for k in row_vrf if not k.startswith('TABLE')]
            for k in sorted(keys):
                display_vrf[k] = row_vrf[k]
            table_addrf = row_vrf['TABLE_addrf']
            rows_addrf = table_addrf['ROW_addrf']
            if not isinstance(rows_addrf, list):
                rows_addrf = [rows_addrf]
            for row_addrf in rows_addrf:
                display_addrf = OrderedDict(display_vrf)
                keys = [k for k in row_addrf if not k.startswith('TABLE')]
                for k in sorted(keys):
                    display_addrf[k] = row_addrf[k]
                table_prefix = row_addrf['TABLE_prefix']
                rows_prefix = table_prefix['ROW_prefix']
                if not isinstance(rows_prefix, list):
                    rows_prefix = [rows_prefix]
                for row_prefix in rows_prefix:
                    display_prefix = OrderedDict(display_addrf)
                    keys = [k for k in row_prefix if not k.startswith('TABLE')]
                    for k in sorted(keys):
                        display_prefix[k] = row_prefix[k]
                    table_path = row_prefix['TABLE_path']
                    rows_path = table_path['ROW_path']
                    if not isinstance(rows_path, list):
                        rows_path = [rows_path]
                    for row_path in rows_path:
                        display_path = OrderedDict(display_prefix)
                        keys = [k for k in row_path if not k.startswith('TABLE')]
                        for k in sorted(keys):
                            display_path[k] = row_path[k]
                        display_table.append(display_path)
        print_table(display_table)
        print()
    return True

def main():
    """ Print documentation; Select a device; Demonstrate; Print command syntax; Print output schema."""
    print(cleandoc(__doc__))
    print()
    
    print('Select an appropriate device from those available.')
    print_table(inventory_config)
    print()
    for device_config in inventory_config:
        try:
            http_session = connect(**device_config)
            try:
                print('Connected to', session_device_url(http_session))
                print()
                demonstrate(http_session)
            finally:
                disconnect(http_session)
        except IOError as ioe:
            log(WARN, 'Unable to connect to Nexus device %s', str(device_config))
            continue
        
        try:
            print('Command Reference:')
            response = cli_schema(http_session, command)
            print_command_schema(response)
            return EX_OK
        except IOError as ioe:
            log(WARN, 'Swallow error retrieving schema(s) for %s %s', str(command), str(ioe))
            print('No schema available for command(s):', command)
            return EX_TEMPFAIL
    
    print("There are no suitable network devices. Demonstration cancelled.")
    return EX_TEMPFAIL

if __name__ == "__main__":
    sys_exit(main())
        
