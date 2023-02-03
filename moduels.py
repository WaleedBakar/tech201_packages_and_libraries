# modules

# a piece of software that imports some sort of functionality
# libraries and modules is as I do not think I explained it too well in the lesson: A module is a collection of code or functions that uses the .py extension - allowing you to use that code/functions in your program A library is a set of RELATED modules or packages bundled together. Modules -> smaller, just code you can useLibraries -> larger/more complex compilations of resources.
import os
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

# when you are buildong a prpgram its really important to think if you need to make a class yourself or to use a function


# Built in functions

# print
# len()
# type()



