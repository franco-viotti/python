### Modules ###

""" Modules are pieces of code that calls other pieces of code
    Prevents us from repeating the same code over and over again. 
    The reserved word *import* is needed
"""

"""
***IMPORTANT***
When importing a module, Python will run all the code that's in that module.
So if the Python file is meant to be imported as a module, is necessary to be careful
not to put side effects at the top-level of the .py file.
"""

import functions

functions.sum_two_values(3, 4)

""" We can also import only functions from a module """
from functions import sum_two_values
sum_two_values(3, 4)

import brais_functions