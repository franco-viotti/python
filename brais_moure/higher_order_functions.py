from functools import reduce

### Higher Order Functions ###
# Functions between functions
# Lets create a simple function

def sum_one(value):
    return value + 1

'''
def sum_two_values_and_add_one(first_value, second_value):
    return first_value + second_value + 1
'''

# Now let's change the below function and include the sum_one function
def sum_two_value_and_add_one(first_value, second_value):
    return sum_one(first_value+second_value)

print(sum_two_value_and_add_one(1, 2))

# We can try adding lambdas
'''
def sum_two_value_and_add_one_w_lambdas(first_value, second_value):
    return lambda first_value, second_value: print(first_value+second_value+1)

a = sum_two_value_and_add_one_w_lambdas(4, 5)
print(f"The result of the function using lambdas is: {a}")
'''
# ! This is not really working

# ? We can pass functions as arguments
def sum_two_values_and_add_one(first_value, second_value, function):
    return function(first_value + second_value)

sum_two_values_and_add_one(1, 2, sum_one)


### Closures ###

def add_ten():
    def add(value):
        return value + 10
    return add

add_closure = add_ten()
print(add_closure(15))

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 30]

# ? Map: the map() function always needs an interable set

def ex_function(number):
    return number*2

print(list(map(ex_function, numbers)))
## ! Prints [4, 10, 20, 42]

## You can also pass a lambda function as a parameter
print(list(map(lambda number: number*2, numbers)))

# ? Filter

def for_filter_greater_than_ten(number):
        return number > 10

print(list(filter(for_filter_greater_than_ten, numbers)))

## You can also pass a lambda function as a parameter
print(list(filter(lambda number: number > 10, numbers)))

# ? Reduce

print(reduce(lambda x, y: x + y, numbers))