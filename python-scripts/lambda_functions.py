"""In python, we use 'lambda' keyword to eclad an anonymous 
function, which is why we refer to them as lambda functions. 
An anonymous function refers to a function declared with no name. 
Altough syntactically they look different, lambda functions behave in
the same way as regular functions that are declared using the 'def' keyword.
A lambda function can take any number of arguments, but they contain only a 
single expression. An expresion is a piece of core executed by the lambda
function, which may or may not return a value.
Lambda functions can be used to return function objects.
Syntactically, lambda functions are restricted to only a single expression."""

#We use the following syntax to create a lambda function

#lambda arguments(s): expression

remainder = lambda num: num % 2
print(remainder(5))
