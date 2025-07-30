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
# ------------------------------------
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
# ------------------------------------
# Assign Multiple Values

a,b,c = 10 , 20 , 30 
print(a)
print(b)
print(c)
# ------------------------------------
# One Value to Multiple Variables
a = b = c = 10 
print(a)
print(b)
print(c)
# ------------------------------------
# Unpack a Collection

fruits = ["apple" , "banana","cherry"]
x,y,z = fruits

print(x)
print(y)
print(z)
# ------------------------------------
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
# ------------------------------------
# The global Keyword

def fun(): 
   global x 
   x = "ahMed"
   print("inside " , x)

fun()
print("outside",x)
# ------------------------------------
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
# ------------------------------------
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
# ------------------------------------
# IN and Not IN

txt = "Ahmed hussein"

print("Ahmed" in txt )     # true
print("Ahmed" not in txt ) # false 

# ------------------------------------

# Slicing 

# possitive index 
x = "ahmed Hussein"
print(x[0:5])
print(x[:5])

print(x[::2]) # two step 

# negative index 
print(x[-13:-8])

# ------------------------------------
# Split 
x = "ahmed H u s sein"
print(x.split(' '))
print(x.split(' ',2)) # split(separator , maxsplit )
# ------------------------------------
# Format 
x = "ahmed"
y = "hussein"
print(f"my name is {x} and my father name is {y}") 
# ------------------------------------
# replace 
x = "ahmed"
print(x.replace('h','A'))
print(x.replace('hme','A'))
# ------------------------------------
# escape characters 

print("ahmed \nhussein") # new line 
print("The date now is 30\\07\\2025") # backSlach 
print("'ahmed'") # without any escape characters 
print('\'ahmed\' ') # to make '' in '' for strings 
print("\"ahmed\"")# to make "" in "" for strings 
print("ahmed\rAHM") # replace Strings after \r in begin the string before \r -> AHMed
print("This is \t tab ")
# ------------------------------------
# String Methods

x = "ahmed"
print(x.upper())
print(x.lower())
print(x.capitalize())

x = "HussEin"
print(x.casefold()) # first letter will be small 

x = "ahmed hussein"
print(x.center(15)) # it see the length of the string and if the prameter is larger it will be move string to center it 

print(x.count("s")) # Count something in string 
