#now that we know what a variable is, lets learn about naming conventions for variables in python.
#first and foremost, variable names should never be one of python's reserved keywords.
'''
return = 5
print(return) 
'''
#this will raise a syntax error because 'return' is a reserved keyword in python.
#heres the code to print all of python's reserved keywords.
import keyword
print(keyword.kwlist)
#next, it is advisable to not use names that are the same as built-in functions or types in python.
'''
len = [1, 2, 3]
print(len)
print(len(len))
'''
#a list is assigned to the variable 'len', which shadows the built-in function 'len()'. the second print statement will raise a TypeError because 'len' is now a list, not a function.
#to avoid this, use variable names that do not conflict with built-in names.
#now that we got certain names out of the way, lets look at some valid ways to name variables in python.
#1. variable names can contain letters, numbers and underscores. Any other special characters are not allowed.
my_variable = 5 #valid
myVariable2 = 10 #valid
_variable_3 = 15 #valid
print(my_variable, myVariable2, _variable_3)
#2. variable names cannot start with a number.
'''
2variable = 20 #invalid
print(2variable)
'''
#note: we do not use _ at the start of generic variable names, even though we can
#it is a convention to use _ for private variables in classes.
#3. variable names are case-sensitive.
myVar = 25
myvar = 30
print(myVar) #prints 25
print(myvar) #prints 30
#below are some conventions to follow when naming variables in python to make your code more readable and maintainable.
#4. variable names should be descriptive and meaningful.
#single character variable names should be avoided unless used in very small scopes like loops or comprehensions.
x = 35 #not descriptive
y = 40 #not descriptive
age = 45 #descriptive
name = 'John' #descriptive
print(x, y, age, name)
#5. for variable names having multiple words, use snake_case (words separated by underscores)
first_name = 'Alice' #snake_case
last_name = 'Smith' #snake_case
full_name = first_name + ' ' + last_name
print(full_name)
#camelCase is used mainly for naming classes in python.
#important note: python now allows unicode characters in variable names
#however, other than niche cases, it is advisable to stick to ASCII characters for better readability and compatibility.