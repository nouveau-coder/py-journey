#another way to check the type of a variable is the isinstance() function
#this function takes two arguments, the variable and the type to check against
#this is useful when we want to check if a variable is of a specific type or a subclass of that type
a = 10         
if isinstance(a, int):
    print("a is an integer")  # this will print as a is indeed an integer
else:
    print("a is not an integer")

b = 3.14
if isinstance(b, int):
    print("b is an integer")
else:
    print("b is not an integer")  # this will print as b is a float

#this code showcases the main difference between type() and isinstance()
print(isinstance(True, int))   # True
print(type(True) is int)       # False
#most of the time, there is no difference between the two, especially for built-in types
#the real difference comes when dealing with inheritance and custom classes, which we will cover later
#for now, you can use either type() or isinstance() to check the type of a