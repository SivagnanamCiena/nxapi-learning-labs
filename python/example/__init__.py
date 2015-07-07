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
This module uses the environment variable NETWORK_PROFILE, which contains the 
name of a Python module. If the path is absolute then the module is loaded from
the absolute location, otherwise the specified module is loaded from directory
<project>/python/config. The module name can omit the file extension '.py'
or '.pyc'.

Examples: 

NETWORK_PROFILE    loads from
---------------    ----------
5node              .../nxapi-learning-labs/python/config/5node.py(c)                 
/home/user/5node   /home/user/5node.py(c)                 

The config file can be located inside or outside the project to make deployment 
easier. That is, if the project is zipped into an egg then there is no need to 
insert a new config file into the egg. The config file does not need to be on 
the Python path. This means you don't need to extend the Python path to your 
config directory or put an __init__.py file with your config file.

Note that the use of an external config file is similar to the industry wide 
use of of external deployment descriptors for services bundled as JAR, WAR or 
EAR files (in the Java universe).

The config file is loaded from the compiled-python file if it exists (extension 
.pyc). It the config file is newer than the compiled file then the compiled 
file is ignored.

The Python package nxapi contains utility functions which are independent of 
this configuration. The modules in package nxapi do not import the config.
Thus the test code can import package nxapi (to test the functions there) 
without any configuration. This is better for unit tests which do not 
require integration to a remote device. For integration testing, the test code 
will load the config and pass the device co-ordinates to the library functions 
(as parameters).

@author: Ken Jarrad (kjarrad@cisco.com)
"""

from __future__ import print_function
import os
from nxapi.context import load_module
from os import getenv
from os.path import join, dirname

inventory_config = []
config_module = None

_default_config_module_dir = join(dirname(__file__), '..', 'config')
_default_config_module_file = 'simulation'

if not inventory_config:
    network_profile = getenv('NETWORK_PROFILE', _default_config_module_file)
    config_module = load_module('config', network_profile, _default_config_module_dir)
    inventory_config = config_module.inventory
    
