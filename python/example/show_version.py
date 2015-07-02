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
Demonstrate how to obtain the version of one network device.
"""
from __future__ import print_function
from inspect import cleandoc
from logging import log, WARN
from nxapi.http import cli_show, connect, disconnect, cli_schema, print_command_schema, session_device_url
from nxapi.context import sys_exit, EX_OK, EX_TEMPFAIL
from nxapi.render import print_table
from example import inventory_config

command = 'sh ver'

def demonstrate(session):
    """ Execute a command, print the output, return True if successful. """
#     print("Execute command '%s' on network device %s" % (command, device_url(**device_config)))
    response = cli_show(session, command)
    for c in response:
        print('Output for command:', c)
        print_table(response[c])
        print()
    return True

def main():
    """ Print documentation; select a device; demonstrate."""
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
        
