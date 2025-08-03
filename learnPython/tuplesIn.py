# () indicate a tuple in Python
# Tuple items are ordered, unchangeable, and allow duplicate values.


t1 = (1,2,2,"ahmed", 2, 3, 4, 5, 6)
print(t1)
# ------------------------------

# Tuples are not changeable (immutable)
t1 = (1,2,3,4,5)
# t1[0]= 100 # error
print(t1)


# but you can change it to list 

t1 = (1,2,3,4,5)
t1 = list(t1)
t1[0] = 100
t1 = tuple(t1)
print(t1)
#--------------------------------

# tuple length

t1=(1,2,3,4,5)
print(len(t1))
# -----------------

t1 = ("ahmed",) # this tuple 
print(type(t1))

notTuple = ("ahmed") # string not tuple 
print(type(notTuple))
#-----------------------------
# Consturctor 
t1 = tuple((1,2,3,4))
print(type(t1))

#------------------------------
# append not working 

t1 = (1,23,3)
t1= list(t1)
t1.append(10)
t1 = tuple(t1)
print(t1)

# concatenate is working

t1 = (1,2,3)
t2= ("ahmed","hussein",2)
t2 = t2 + t1
print(t2)
# -----------------
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# unpackage tuple 
fruits = ("apple", "banana", "cherry")

green, yellow, red = fruits

print(green)
print(yellow)
print(red)
# -------------------------
#If the number of variables is less than the number of values,
#  you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# -------------
# Method

t1 = (1,2,1,1,1,1,3)
print(t1.count(1))

t1 = ("ahmed", "hussein")
print(t1.index("ahmed"))

#----------------------------
