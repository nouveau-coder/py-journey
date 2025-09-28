#now let us move on to boolean values
#boolean values can be either True or False
bool1 = True    #this is a boolean value representing true
bool2 = False   #this is a boolean value representing false
print(bool1)    #this will print the boolean value True
print(bool2)    #this will print the boolean value False
#this is a very important data type in programming as it is used in conditional statements and loops
#most python values are True by default
print(bool(1))        #this will print True as 1 is considered True
print(bool(0))        #this will print False as 0 is considered False
print(bool("Hello"))  #this will print True as non-empty strings are considered True
print(bool(""))       #this will print False as empty strings are considered False
print(bool([]))       #this will print False as empty lists are considered False
print(bool([1, 2, 3]))#this will print True as non-empty lists are considered True
#note: we have a special type called NoneType which has a single value None
print(bool(None))     #this will print False as None is considered False
