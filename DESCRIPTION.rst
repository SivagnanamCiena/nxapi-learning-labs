NX-API Learning Labs
=======================

Sample usage of NX-API.

All commands shown below assume that your current working directory is the top level directory of the project. 

Directory python/example contains scripts that are executable from the command line.

e.g. in bash

$ python/example/show_version.py

To add this project to your Python path using pip:

$ pip install -e .

To uninstall:

$ pip uninstall nxapi-learning-labs

If using pip is not satisfactory then use setup.py directly:

$ python setup.py develop

To uninstall

$ python setup.py develop --uninstall

Of course you may need to prefix all the above commands with 'sudo' to authorise them.

To verify that the Python path is correct, use command:

$ python/example/python_path.py

A list of directories will appear. One directory in that list should be the top level directory of the project, suffixed with sub-directory 'python'.

e.g. using bash, the second list entry verifies that the project is on the Python path.

sys.path
--------
/home/<user>/git/nxapi-learning-labs/python/example
/home/<user>/git/nxapi-learning-labs/python
/usr/lib/python2.7
/usr/lib/python2.7/plat-x86_64-linux-gnu
/usr/lib/python2.7/lib-tk
/usr/lib/python2.7/lib-dynload
/usr/local/lib/python2.7/dist-packages
/usr/lib/python2.7/dist-packages
/usr/lib/python2.7/dist-packages/PILcompat
/usr/lib/python2.7/dist-packages/gtk-2.0
/usr/local/lib/python2.7/dist-packages/future-0.14.3-py2.7.egg
/usr/lib/python2.7/lib-old

