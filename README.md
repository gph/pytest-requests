## API unittest with PyTest

Simple example how to mock module requests using PyTest.

### How to run?
```commandline
$ pytest
================================= test session starts =================================
platform win32 -- Python 3.10.5, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\gph19\Desktop\pytest-api-unittest
plugins: cov-4.0.0, mock-3.10.0
collected 3 items

tests\test_get_data.py ...                                                       [100%] 

================================== 3 passed in 0.10s ==================================
```

### How to check coverage?
```commandline
$ pytest --cov
================================= test session starts =================================
platform win32 -- Python 3.10.5, pytest-7.2.1, pluggy-1.0.0
rootdir: C:\Users\gph19\Desktop\pytest-api-unittest
plugins: cov-4.0.0, mock-3.10.0
collected 3 items

tests\test_get_data.py ...                                                       [100%]

---------- coverage: platform win32, python 3.10.5-final-0 -----------
Name                     Stmts   Miss  Cover
--------------------------------------------
main.py                      9      0   100%
tests\__init__.py            0      0   100%
tests\test_get_data.py      20      0   100%
--------------------------------------------
TOTAL                       29      0   100%


================================== 3 passed in 0.22s ================================== 
```