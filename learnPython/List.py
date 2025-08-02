# Lists are used to store multiple items in a single variable.
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed.
# Lists are created using square brackets.

# ordered
myList = ["apple", "banana", "cherry"]
print(myList)
print(len(myList))

# allow duplicate
myList = ["apple", "banana", "cherry" , "apple"]
print(myList)
print(len(myList))
print(type(myList))

# changeable 
myList = ["apple", "banana", "cherry"]
myList[0] = 10 
myList[1]= "ahmed"
print(myList)

# allow multi type 
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["ahmed",2005, True]
print(type(list1[0]))
print(type(list2[0]))
print(type(list3[0]))
print(type(list4[0]))

# Constructor 

thisList = list(("apple", "banana" , "cherry "))
print(thisList)
print(type(thisList))

# Access Item
myList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(myList[0])
print(myList[-1])

print(myList[2:5]) # search will start at index 2 (included) and end at index 5 (not included).
print(myList[:4]) # By leaving out the start value, the range will start at the first item.
print(myList[2:]) # By leaving out the end value, the range will go on to the end of the list.

print(myList[-4:-2])
print(myList[-4:])

# Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change List Items

myList = ["ahmed" , "hussein" , "ahmed", "mohammed", "salh"]
myList[0:2] ="a"
print(myList)

myList = ["ahmed" , "hussein" , "ahmed", "mohammed", "salh"]
myList[0:2] =["a","a","a","a","a","a","a","a","a"]
print(myList)

# -------------------------
# insert 

myList = ["apple", "banana", "cherry"]
myList.insert(1, "watermelon")
print(myList)


myList = ["apple", "banana", "cherry"]
myList.insert(1, ["watermelon","ahmed"])# add list to end (list in list ) 
print(myList)

# append 

thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # add one element to end 
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.append(["orange" , "al",'asdf']) # add list to end (list in list ) 
print(thislist[3][1])

# --------------
# extend 

thislist = ["apple", "banana", "cherry"]
myList = ["mango", "pineapple", "papaya"]
thislist.extend(myList)
print(thislist)
print(myList)



thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange") # tuple 
thislist.extend(thistuple)
print(thislist)

# Error 
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange") # tuple 
# thistuple.extend(thislist)
# print(thistuple)

# ----------------------
# remove element in list 

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# delete the first one 
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# removed specify index 

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# remove last element 
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# with del 

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

del thislist[1]
print(thislist)

# del all list

thislist = ["apple", "banana", "cherry"]
del thislist
print(thisList) # not defined 

# clear list content 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # -> []

# ---------
# loop 

mylist = ["apple", "banana", "cherry"]
for i in mylist:
  print(i)

for i in range(len(mylist)):
  print(mylist[i])

# list comprehension 


# newlist = [expression for item in iterable if condition == True]

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index) + ": " + str(area))



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# equivalent to

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [ x for x in fruits if "a" in x]
print(newlist)

# --------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [ x for x in fruits if x != "apple"]
print(newList)
newList = [x for x in fruits]
print(newList)

# -------------------------------------

x = [i for i in range(10)]
print(x,"\n")

x = [i for i in range(10) if i < 5]
print(x,"\n")

# ----------------------------------

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits = [x.upper() for x in fruits]
print(fruits, "\n")

newlist = ["hello" for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
i = [x if x != "banana" else "orange" for x in fruits]
print(i)

#---------------------------------
# Sort List 

List = [2,5,6,3,1,4]
List.sort()
print(List) 

List.sort(reverse= True) 
print(List)


def myfunc(n):
  return abs(n - 50)

thislist.sort(key = myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key= str.lower)
print(thislist)



thislist = [100, 50, 65, 82, 23]
thislist.reverse()
print(thislist)

# --------------------------------
# Copy List

# don't copy like this 
list1 = ["ahmed" , "hussein" , "ahmed"]
list2 = list1
list2[0] = 100
print(list1[0] , list2[0])
# this is shadow copy ,
#  because: list2 will only be a reference to list1,
#  and changes made in list1 will automatically also be made in list2.

# use list() method 

list1 = ["ahmed" , "hussein" , "ahmed"]
list2 = list(list1)
list2[0] = 100
print(list1[0] , list2[0])

# use this slice operator 
list1 = ["ahmed" , "hussein" , "ahmed"]
list2 = list1[:]

list2[0] = 100
print(list1[0] , list2[0])
print(list2)

#--------------------------------
# join two list 

# First Method 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# second method

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for i in list1:
  list2.append(i)

print(list2)

# Third Method 

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list2.extend(list1)
print(list2)
