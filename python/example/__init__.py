from __future__ import print_function
import imp
import os
from os import getenv

inventory_config = []
inventory_config_path = None

def load_config_module(module_file_name):
    (module_file_name, _) = os.path.splitext(module_file_name)
    if '/' in module_file_name:
        uri = module_file_name
    else:
        uri = os.path.join(os.path.dirname(__file__), '..', 'config', module_file_name)
        uri = os.path.normpath(uri)
    source_file_name = uri + '.py'
    compiled_file_name = uri + '.pyc'
    if os.path.exists(compiled_file_name):
        if os.path.exists(source_file_name) \
        and os.path.getmtime(source_file_name) > os.path.getmtime(compiled_file_name): 
                config_module = imp.load_source('config', source_file_name)
                config_module_path=source_file_name
        else:
            config_module = imp.load_compiled('config', compiled_file_name)
            config_module_path=compiled_file_name
    elif os.path.exists(source_file_name):
        config_module = imp.load_source('config', source_file_name)
        config_module_path=source_file_name
    else:
        raise ImportError('Config module not found:', uri)
    global inventory_config
    inventory_config = config_module.inventory
    global inventory_config_path
    inventory_config_path = config_module_path

if not inventory_config:
    network_profile = getenv('NETWORK_PROFILE', 'simulation')
    load_config_module(network_profile)
    
