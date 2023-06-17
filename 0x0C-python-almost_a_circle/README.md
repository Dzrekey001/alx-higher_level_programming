#Python - Almost a Circle#

This project is part of the Higher Level Curriculum at ALX School. It is designed to reinforce and test your understanding of various Python concepts, including object-oriented programming, unit testing, file I/O, and JSON serialization/deserialization.

The project is divided into multiple tasks, each building upon the previous one. The goal is to create a set of classes and methods that simulate a rectangle and a square, while also implementing important features such as attribute validation, area calculation, display, and updating.
***
#Learning Objectives#
By completing this project, you will gain knowledge and practical experience in the following areas:

1. Implementing unit tests in a large project
2. Serializing and deserializing Python objects
3. Working with JSON files
4. Understanding and using *args and **kwargs
5. Handling named arguments in functions

***
#Requirements#
1. Python scripts should be written and executed using Python 3.8.5 on Ubuntu 20.04 LTS.
2. The pycodestyle tool (version 2.8.*) should be used to validate the code style.
3. All files must be executable and end with a new line.
4. The first line of each file should be #!/usr/bin/python3.
5. A README.md file is mandatory and should be placed at the root of the project folder.
6. Documentation should be provided for all modules, classes, and functions.
7. All files, classes, and methods must be unit tested and comply with PEP 8 style guidelines.
***
#Project Structure#
The project is organized as follow

```shell
0x0C-python-almost_a_circle/
├── models/
│   ├── __init__.py
│   ├── base.py
│   └── rectangle.py
└── tests/
    ├── __init__.py
    └── test_models/
        ├── __init__.py
        └── test_base.py
```

The models directory contains the Python package for the project, including the __init__.py file.

The models directory also contains the base.py and rectangle.py files, which define the Base and Rectangle classes, respectively.

The tests directory contains unit tests for the project. It follows the same structure as the models directory.

**How to Use**
To use the project, follow these steps:

Clone the repository: git clone https://github.com/your_username/alx-higher_level_programming.git

Navigate to the project directory: cd 0x0C-python-almost_a_circle

Run the unit tests: python3 -m unittest discover tests

You can also test individual files or modules using the python3 -m unittest command with the desired test file.

Author
This project was completed as part of the ALX School curriculum.
