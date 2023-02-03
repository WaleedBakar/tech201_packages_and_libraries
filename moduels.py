# modules

# a piece of software that imports some sort of functionality
# a module is you referring to a file
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



