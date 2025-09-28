#now that we have seen numbers, let's look at strings
#strings are used to represent text
#in python, strings are enclosed in either single quotes or double quotes
str1 = 'Hello, World!'   #this is a string using single quotes
str2 = "Hello, Python!"   #this is a string using double quotes
print(str1)               #this will print the first string
print(str2)               #this will print the second string
#we can also use triple quotes for multi-line strings
str3 = '''This is a
multi-line
string.'''
print(str3)               #this will print the multi-line string
#we can concatenate strings using the + operator
str4 = str1 + " " + str2
print(str4)               #this will print the concatenated string
#we can also repeat strings using the * operator
str5 = str1 * 3
print(str5)               #this will print the first string three times