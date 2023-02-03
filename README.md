# tech201_packages_and_libraries
tech201_packages_and_libraries
# Modules

a piece of software that imports some sort of functionality
libraries and modules is as I do not think I explained it too well in the lesson: A module is a collection of code or functions that uses the .py extension - allowing you to use that code/functions in your program A library is a set of RELATED modules or packages bundled together. Modules -> smaller, just code you can useLibraries -> larger/more complex compilations of resources.
import os
```` python
import math,datetime, sys

working_directory = os.getcwd()
print(working_directory)

def return_user_id():
    print(os.getpid())


def return_user_name():
    print(os.uname())

print(datetime.date.today())

print((sys.path))

print(math.remainder(1, 5))
``````
 when you are buildIng a program its really important to think if you need to make a class yourself or to use a function


# Built in functions
```` 
print len() 
type()

```
pip and packages

pipi is Pythons package manager and installer

import requests

 requests_bbc = requests.get("https://www.bbc.co.uk")

 print(requests_bbc.status_code)

 print(requests_bbc.content)
``````

# Python libraries

# import random
```` python
from random import random
import math

print(random())

num_float = 23.66
print(math.ceil(num_float))

print(math.floor(num_float))

print((math.pi))

`````
