Tests
-----

This folder contains unit and validations tests for the Blender glTF 2.0 exporter.

The unit tests are implemented in the `unit_test.py` file. For convenience, a Windows batch file exists having the default parameters set and using the standard installation path for Blender under Windows.  
Execute `unit_test.bat` to run the unit tests.

For the validation tests, several tests do exist and all of them have the patern `vt_XX_*.py` where `XX` is an increasing number of the test and `*` is a descriptive string.
Also for the validation tests, Blender is used and for convenience, the batch script `validation_test.bat` does exist.  
To run these tests, execute `validation_test.bat [FILENAME]` e.g. `validation_test.bat vt_02_all_scenes`.