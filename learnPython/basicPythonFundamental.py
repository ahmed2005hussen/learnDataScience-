# ------------------------------------------
# Author: Ahmed Hussein Ahmed
# ------------------------------------------

# ✅ Python Version
# - Use `sys.version` to check the installed Python version.

# ✅ Comments
# - Single-line comments use `#`.
# - Multi-line comments can be done using triple quotes `""" """`.

# ✅ Variables
# - Python is dynamically typed, no need to declare variable types.
# - Examples with `int`, `float`, `str`.

# ✅ Variable Naming Rules
# - Legal: my_var, _myvar, myVar, MYVAR, myvar2
# - Illegal: 2myvar, my-var, my var

# ✅ Multiple Assignment
# - Assign multiple variables in one line: `a, b, c = 1, 2, 3`
# - Same value to multiple variables: `a = b = c = 10`
# - Unpacking a collection: `x, y, z = [1, 2, 3]`

# ✅ Global vs Local Scope
# - Variables declared outside functions are global.
# - Use `global` keyword to modify global variables inside functions.
# - Variable shadowing: local variables can mask global ones inside a function.

# ✅ Data Types Overview
# - str, int, float, complex
# - list, tuple, range
# - dict
# - set, frozenset
# - bool
# - bytes, bytearray, memoryview
# - NoneType

# ✅ `print()` Enhancements
# - Use `end=""` to control line endings in print statements.


# To know The version for python 
import sys
print(sys.version)
print("\n \n")

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
print("\n \n")

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
print("\n \n")

# ------------------------------------
# One Value to Multiple Variables
a = b = c = 10 
print(a)
print(b)
print(c)
print("\n \n")

# ------------------------------------
# Unpack a Collection

fruits = ["apple" , "banana","cherry"]
x,y,z = fruits

print(x)
print(y)
print(z)
print("\n \n")

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
print("\n \n")

# ------------------------------------
# The global Keyword

def fun(): 
   global x 
   x = "ahMed"
   print("inside " , x)

fun()
print("outside",x)
print("\n \n")

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

# ------------------------------

print("ahmed" , end=",")
print("ahmed" , end="")