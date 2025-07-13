# To know The version for python 
import sys
print(sys.version)
# --------------------------------
# Comments

# this is single line Commment

"""
This is a 
mulite line comment 
"""
# --------------------------------
# Variables 

a = 10      # this is int 
b = "ahmed" # this is str 
c = 'ahmed' # this is str 
d = 10.1    # this is float 

print("The Type of ","'a' is ",type(a))
print("The Type of ","'b' is ",type(b))
print("The Type of ","'c' is ",type(c))
print("The Type of ","'c' is ",type(d))

# Variablse Name 

# Legal Names
myvar   = "Ahmed"
my_var  = "Ahmed"
_my_var = "Ahmed"
myVar   = "Ahmed"
MYVAR   = "Ahmed"
myvar2  = "Ahmed"

#Illegal Names

"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

# Assign Multiple Values

a,b,c = 10 , 20 , 30 
print(a)
print(b)
print(c)

# One Value to Multiple Variables
a = b = c = 10 
print(a)
print(b)
print(c)

# Unpack a Collection

fruits = ["apple" , "banana","cherry"]
x,y,z = fruits

print(x)
print(y)
print(z)

# Global Variables

x = "awesome"
def sum(): 
    print("pyton is : " , x)

sum()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
  x = "ahmed"
myfunc()

print("Python is " + x)

# The global Keyword

def fun(): 
   global x 
   x = "ahMed"
   print("inside " , x)

fun()
print("outside",x)

# Data Type in python 

"""

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
#  Data Types 
x = "Hello World"	
print(type(x))

x = 20		
print(type(x))	

x = 20.5		
print(type(x))	

x = 1j		
print(type(x))	

x = ["apple", "banana", "cherry"]		
print(type(x))	

x = ("apple", "banana", "cherry")		
print(type(x))	

x = range(6)		
print(type(x))	

x = {"name" : "John", "age" : 36}		
print(type(x))	

x = {"apple", "banana", "cherry"}		
print(type(x))	

x = frozenset({"apple", "banana", "cherry"})		
print(type(x))	

x = True		
print(type(x))	

x = b"Hello"		
print(type(x))	

x = bytearray(5)		
print(type(x))	

x = memoryview(bytes(5))		
print(type(x))	

x = None
print(type(x))	

