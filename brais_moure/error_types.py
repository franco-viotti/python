### Error Types ###

# SyntaxError
print "Hello world!" # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# NameError
print(name) # NameError: name 'name' is not defined

# IndexError
list = [1, 2, 3, 4, 5]
print(list[10]) # IndexError: list index out of range

# ModuleNotFoundError
import maths # ModuleNotFoundError: No module named 'maths'

# AttributeError
import math
print(math.PI) # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

# KeyError
dict = {1:2, 3:4, 5:6, 7:8}
print(dict[24]) # KeyError: 24

# TypeError
print(list["Something"]) # TypeError: list indices must be integers or slices, not str

# ImportError
from math import PI # ImportError: cannot import name 'PI' from 'math' (unknown location)

# ValueError
my_int = int("10 años") # ValueError: invalid literal for int() with base 10: '10 años'

# ZeroDivisionError
print(1/0) # ZeroDivisionError: division by zero
