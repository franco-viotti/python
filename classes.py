### Classes ###

# The reserved word class is used

class Person: #This is enough to define the class
    pass    # pass is a null statement. The interpreter does not ignore this but nothing happens
            #is useful when you don't want to write the implementation of a function now

#What if we need a class with its constructor
class Person_constructor:
    def __init__(self, name, surname) -> None: #Now the class is able to receive parameters
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"
        self.__private_attribute = "You cannot access me" 

    def walk(self):
        print(f"{self.name} is walking")


    
someone = Person_constructor("John", "Doe")
print(someone.name, someone.surname)
print(someone.full_name)
print(someone.walk())