class MyClass:
  x = 5

y = MyClass.x = 100 
print(y)

# Constructor 

# The self Parameter:
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.

# It does not have to be named self, you can call it whatever you like, 
# but it has to be the first parameter of any function in the class:
class Person: 
  def __init__(self ,name ,age):
    self.name = name
    self.age = age  

person1 = Person("ahmed", 20)
print(f"Name: {person1.name} , age: {person1.age}")

# -----------------------------
# لما تحاول تطبع كائن من كلاس، بايثون بيحاول يحوله لسترنج علشان يعرضه.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
# ------------------
# __str__ :
# هي اللي بتقول لبايثون: لو حد حاول يطبعني أو يحولني لـ استرينج أرجع له النص ده".
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# -------------------------
# Create Methods

class Person: 
  def __init__(self , name , age): 
    self.name = name 
    self.age = age
  
  def myFunc(self):
    print(f"Hello {self.name}")

p1 = Person("Ahmed" , 20)
p1.myFunc()

# -----------------------
# Delete Object Properties

class Person: 
  def __init__(self , name , age): 
    self.name = name 
    self.age = age

del Person.age
p1 = Person("Ahmed" , 20)
# print(p1.age) error 

# Delete Objects

class Person: 
  def __init__(self , name , age): 
    self.name = name 
    self.age = age

p1 = Person("Ahmed" , 20)
del p1
# print(p1.age) error 

# --------------------------------------

# Inheritance 

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Student(Person): 
  def __init__(self,fname,lname):
    Person.__init__(self ,fname,lname) 

x = Student("ahmed",20)
x.printname()

# Or use super method 

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Student(Person): 
  def __init__(self,fname,lname , year):
    super().__init__(fname,lname)
    self.graduationyear = year

x = Student("ahmed",20,2027)
x.printname()
print(x.graduationyear)

# -------------------------------
# Polymorphism

# The word "polymorphism" means "many forms",
# and in programming it refers to methods/functions/operators
# with the same name that can be executed on many objects or classes.

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

# ----------------------
