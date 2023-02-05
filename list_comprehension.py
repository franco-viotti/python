### List Comprehension ###
#First, we need to create a list 

my_original_list = [35, 24, 62, 53, 30, 30, 17]

#We can create a different list from an older list
my_list = [iterator for iterator in my_original_list]
print(my_list)

#Another way to create a list 
range_list = [iterator for iterator in range(80)]
#print(range_list)

#Also 
modified_list = [iterator+1 for iterator in range(7)]
print(modified_list)

#It's even possible to create a function and then use it inside the list
def add_five(number):
    return number+5

added_list = [add_five(iterator) for iterator in range(7)]
print(added_list)
