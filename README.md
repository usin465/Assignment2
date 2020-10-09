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

## Testing

Testing requires files 235_WebApp --> tests --> unit where test files are located for testing the memory repository.
Domain model testing is omitted as was comprehensively tested in A1.
To view test results change configuration to run the tests specified.
Current config may be running on wsgi, thus will need to be changed to the specific test.


 