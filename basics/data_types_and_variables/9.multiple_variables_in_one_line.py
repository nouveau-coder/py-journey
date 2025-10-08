#python has a neat little trick to assign multiple variables in one line
#usually beginners write code like this
var1 = 10
var2 = 20
var3 = 30
print(var1)  #this will print 10
print(var2)  #this will print 20
print(var3)  #this will print 30
#too many lines for just three variables, right?
#we can do the same thing in one line
var1, var2, var3 = 10, 20, 30
print(var1)  #this will print 10
print(var2)  #this will print 20
print(var3)  #this will print 30
#this is called unpacking
#we can also assign the same value to multiple variables in one line
a = b = c = 100
print(a)  #this will print 100
print(b)  #this will print 100
print(c)  #this will print 100
#this is called chained assignment
