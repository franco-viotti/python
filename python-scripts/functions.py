### Functions ####
# The reserved word *def* is used

def function_name():
    print("This is a function")

# Now we call the function

function_name()

#Ok but what about parameters

def sum_two_values(a, b) -> int:
    print(a + b)

sum_two_values(1, 2.2)

###
# This is useful when you want to create a function with one
# parameter that, if it is not given, will have some default value
# anyway.
# ###
def print_name_with_default_parameter(name, surname, alias = "None"):
    print(f"{name} {surname} {alias}")

print_name_with_default_parameter("Brais", "Moure")

### How to create a function that receives infinite parameters
def dynamic_parameter_function(*texts_we_wanna_print):
    print(texts_we_wanna_print)

dynamic_parameter_function("Hi", "Moure", "Brais")