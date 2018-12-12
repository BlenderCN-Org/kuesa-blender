To run the tests:
1. Move into the addons/kuesa folder
2. Run ./launch_tests.sh

Note: When running a python script with blender -P, keep in mind that blender
uses his own python interpreter, that the sys.path to resolve includes isn't
modifiable by setting PYTHONPATH and that modules or packages in the current
directory won't resolve either.
