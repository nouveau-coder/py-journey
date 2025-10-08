#sometimes we need to convert one data type to another
#this is called type conversion
#either we can do it implicitly or explicitly
#implicit type conversion is done automatically by python
var1 = 10        #this is an integer
var2 = 3.14      #this is a float
var3 = var1 + var2  #here, var1 is implicitly converted to float
print(var3)      #this will print 13.14
print(type(var3))#this will print <class 'float'>
#explicit type conversion is done using built-in functions like int(), float(), str(), etc.
var4 = 10.99     #this is a float
var5 = int(var4) #here, var4 is explicitly converted to int
print(var5)      #this will print 10
print(type(var5))#this will print <class 'int'>
var6 = 20        #this is an integer
var7 = str(var6) #here, var6 is explicitly converted to string
print(var7)      #this will print '20'
print(type(var7))#this will print <class 'str'>
var8 = "3.14"    #this is a string
var9 = float(var8)#here, var8 is explicitly converted to float
print(var9)      #this will print 3.14
print(type(var9))#this will print <class 'float'>
#note: when converting from float to int, the decimal part is truncated, not rounded
var10 = 9.99
var11 = int(var10) #this will be 9, not 10
print(var11)       #this will print 9
print(type(var11)) #this will print <class 'int'>
#you can also convert complex numbers to other types, but only the real part is considered
var12 = 2 + 3j
var13 = int(var12.real) #this will be 2
print(var13)            #this will print 2
print(type(var13))      #this will print <class 'int'>
#be careful while converting strings to numeric types, the string must represent a valid number
var14 = "100"
var15 = int(var14)      #this will be 100
print(var15)            #this will print 100
print(type(var15))      #this will print <class 'int'>
var16 = "Hello"
#var17 = int(var16)     #this will raise a ValueError