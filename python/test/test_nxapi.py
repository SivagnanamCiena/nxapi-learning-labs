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

from unittest.case import TestCase
from nxapi.context import load_module 
from os.path import splitext, split
class Test(TestCase):

    def test_load_module(self):
        # Load a known module, so we expect the load to succeed.
        # We'll specify the module name, though.                  
        module_a = load_module('a', __file__, None)
        self.assertEqual(module_a.__name__, 'a')

        # Do the same with a different name to ensure it doesn't hit a cache.         
        module_b = load_module('b', __file__, None)
        self.assertEqual(module_b.__name__, 'b')

        # Specify the file path components separately.
        (module_dir, module_name) = split(__file__)
        module_c = load_module('c', module_name, module_dir)
        self.assertEqual(splitext(module_c.__file__)[0], splitext(__file__)[0])

        # Remove file extension.  
        (module_name, _) = splitext(module_name)
        module_d = load_module('d', module_name, module_dir)
        self.assertEqual(splitext(module_d.__file__)[0], splitext(__file__)[0])

        # Try loading a module that does not exist.
        try:
            load_module('e', 'non-existing-file', module_dir)
            self.fail('Expected ImportError')
        except ImportError as _:
            pass