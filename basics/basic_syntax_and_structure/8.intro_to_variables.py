#now that we got a basic understanding of python syntax, let's learn about variables.
#unlike some other programming languages, python does not require you to declare a variable before using it.
#variables are only references to objects in memory, unlike other programming languages where variables are containers for data.
a = 'hello'
print(a)  #this line of code will print the value of the variable 'a' to the console.
b = 5
print(b) #this line of code will print the value of the variable 'b' to the console.
a = b 
print(a) #this line of code will print the value of the variable 'a' to the console. since we assigned the value of 'b' to 'a', it will print 5.
# we can see that we do not need to declare the variable type. python is a dynamically typed language, meaning that the type of a variable is determined at runtime.