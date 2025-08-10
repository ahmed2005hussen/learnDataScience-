def printHelloWorld(name):
    print(f"Hello World : {name}")

printHelloWorld("ahmed")

# --------------------------
# pass list 
def hello(*args):
    print("hello " + args[2])

hello("ahmed" , 3, "hussein")
# ------------------------------
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# pass dic
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# ---------------------------
# default value 
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# passing list 
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
# --------------------
# return value  

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
# ------------------
def my_function(x, /):
  print(x)

my_function(3)
# my_function(x = 3) will give an error 


def my_function(x):
  print(x)

my_function(x = 3)

# ----------------------------

def my_function(*, x):
  print(x)

my_function(x = 3)
# my_function(3) error  

# Lambda function

#Syntax: lambda arguments : expression
x = lambda a : a + 10 
print(x(10))

x = lambda a,b: a*b
print(x(2,3))
# -----------------------
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
#---------------------------
