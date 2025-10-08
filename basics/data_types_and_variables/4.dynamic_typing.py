#python is a dynamically typed language
#this means that we do not need to declare the data type of a variable while creating it
#so we can reassign a variable to a different data type
var = 10        #this is an integer
print(var)      #this will print 10
print(type(var))#this will print <class 'int'>
var = 3.14      #now var is reassigned to a float
print(var)      #this will print 3.14
print(type(var))#this will print <class 'float'>
var = "Hello"   #now var is reassigned to a string
print(var)      #this will print Hello
print(type(var))#this will print <class 'str'>
#this feature is due to the fact that python variables are just labels pointing to objects in memory
#in some other programming languages like C, C++, Java, etc., variables act as storage locations with a fixed data type