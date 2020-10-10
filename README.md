# COMPSCI 235 Assignment 2 - Movie Web App

## Description

A Web application that demonstrates use of Python's Flask framework. The application makes use of libraries such as the Jinja templating library. Architectural design patterns and principles including Repository, Dependency Inversion and Single Responsibility have been used to design the application. Testing includes unit and repository testing using the pytest tool. 

## Installation

**Installation via requirements.txt**

```shell
$ cd 235_Webapp
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

When using PyCharm, set the virtual environment using 'File'->'Settings' and select '235_WebApp' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 

## Execution

**Running the application**

From the *235_WebApp* directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

````shell
$ flask run
```` 

## Configuration

The *235_WebApp/.env* file contains variable settings. They are set with appropriate values.

* `FLASK_APP`: Entry point of the application (should always be `wsgi.py`).
* `FLASK_ENV`: The environment in which to run the application (either `development` or `production`).
* `SECRET_KEY`: Secret key used to encrypt session data.
* `TESTING`: Set to False for running the application. Overridden and set to True automatically when testing the application.


## Testing

Testing requires that file *235_WebApp/tests/conftest.py* be edited to set the value of `TEST_DATA_PATH`. You should set this to the absolute path of the *235_WebApp/tests/data* directory. 

You can then run tests from within PyCharm.


Note - unit testing for the domain model has been omitted. This is due to the extensive testing already carried out in A1. As a result, we can assume that the existing domain model is fully functional due to passing all tests in coderunner.


 