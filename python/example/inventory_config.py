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
List of configuration information of each device in the inventory.

@author: Ken Jarrad (kjarrad@cisco.com)
"""
from __future__ import print_function
from inspect import cleandoc
from logging import log, WARN
from nxapi.http import  connect, disconnect, session_device_url
from nxapi.context import sys_exit, EX_OK, EX_TEMPFAIL
from nxapi.render import print_table
from example import inventory_config, config_module
from inspect import getfile

def main():
    """ Print documentation; Print configuration of each device."""
    print(cleandoc(__doc__))
    print()
    
    print('Loaded from:', getfile(config_module))
    print()
    
    if not inventory_config:
        print("There are no network devices configured.")
        return EX_TEMPFAIL

    print('Configured devices.')
    print_table(inventory_config)
    print()
    
    exit_code = EX_OK
    for device_config in inventory_config:
        try:
            http_session = connect(**device_config)
            print('Connected to', session_device_url(http_session))
            disconnect(http_session)
        except IOError:
            log(WARN, 'Unable to connect to Nexus device %s', str(device_config))
            exit_code = EX_TEMPFAIL
            continue
    return exit_code

if __name__ == "__main__":
    sys_exit(main())
        
