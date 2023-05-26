### Lambdas ###

# Lambdas are functions. They have no name, so they're different that
# normal functions.
# ! For creating lambdas, we use the reserved word 'lambda'

lambda first_parameter, second_parameter: first_parameter + second_parameter

# ? A lambda function does not have a name, so how can I call for it?
# We can save the lambda function in a variable for it's later usage

add_two_values = lambda first_parameter, second_parameter: first_parameter + second_parameter
add_two_values(2, 3)

# We can also introduce lambdas into another function
# For example
def add_three_values(value):
    return lambda first_parameter, second_parameter: first_parameter + second_parameter + value

print(add_three_values(1)(2, 3))
