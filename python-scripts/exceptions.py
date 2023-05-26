### Exception Handling ###
### We need to handle possible exceptions or errors that an app might have

#This mechanism is useful when something goes wrong in the try statement, so
#the except statement continues execution withouth stoping the program. Also, 
#we don't need to analyze every possible exception, we can handle any of them.

try:
    print("3"+ 4)
except:
    print("something else went wrong")
else: 
    print("the execution goes on. This will execute whenever there is no exception")
finally:
    print("this goes forward every time")

#We can also declare what kind of exception we are trying to catch
try:
    print("3"+ 4)
except (ValueError, TypeError):
    print("something else went wrong")
else: 
    print("the execution goes on. This will execute whenever there is no exception")
finally:
    print("this goes forward every time")


#And we can capture the excpetion information too
#If an exception occurs, we will want to know what kind of exception it is
try:
    print("3"+ 4)
except TypeError as type:
    print(type)
else: 
    print("the execution goes on. This will execute whenever there is no exception")
finally:
    print("this goes forward every time")