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

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index) + ": " + str(area))