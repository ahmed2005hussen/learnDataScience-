# ------------------------------------------------------------
# File Description:
# This file is a hands-on practice with Python dictionaries.
# It covers the most important operations you can perform on them:
#
# 1️⃣ Creating a Dictionary:
#     - Using {} or the dict() constructor.
#
# 2️⃣ Modifying items:
#     - Changing the value of an existing key.
#     - Adding new key-value pairs.
#
# 3️⃣ Lists inside a Dictionary:
#     - Storing lists as values.
#     - Looping through keys and values with .items().
#
# 4️⃣ Accessing items:
#     - Directly by key: thisdict["key"].
#     - Using the .get() method.
#
# 5️⃣ Getting keys and values:
#     - .keys() to view all keys.
#     - .values() to view all values.
#     - .items() to view keys and values together.
#
# 6️⃣ Important note:
#     - Keys and values are "views", meaning changes to the dictionary
#       will be reflected in these views immediately.
#
# 7️⃣ Checking if a key exists:
#     - Using "in" and "not in".
#
# 8️⃣ Updating items:
#     - Using .update() to modify or add items.
#
# 9️⃣ Removing items:
#     - .pop(key) removes a key-value pair by key.
#     - .popitem() removes the last inserted item.
#     - del thisdict[key] removes a key-value pair by key.
#
# 🔟 Looping through a dictionary:
#     - Keys only: for key in dict.keys()
#     - Values only: for value in dict.values()
#     - Keys and values: for key, value in dict.items()
#
# 1️⃣1️⃣ Copying a dictionary:
#     - Using .copy().
#     - Using dict(existing_dict).
#
# ------------------------------------------------------------


# Dictionary items are ordered, changeable, and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(type(thisdict))
# modify on your dic
thisdict["brand"] = "BMW"
print(thisdict)

# list in dic

thisdict = {
  "brand": ["Ford" , "BMW" , "marcides" , "kia"],
  "model": ["Mustang", "B" , "M" , "k"],
  "year":  [1964, 2013,2011, 2005]
}

for key , value in thisdict.items():
    print(key , value)
#-----------------------
# constractor 

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
# accessing items 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

# to know keys 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.keys())


# to know values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.values())



# to know both

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.items())

# -----------------
# The list of the values is a view of the dictionary,
#  meaning that any changes done to the dictionary will be reflected in the values list.


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# --------------------------------
# check if key exist 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model"  in thisdict: 
    print("yes")

if "ahmed" not in thisdict:
    print("no")
# ------------------------
 
# update function 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020 , "brand" : "bmw" , "ahmed" : "hussein"})
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.popitem() # delete the last 
print(thisdict)

del thisdict["year"]
print(thisdict)

# looping 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# to loop in key 

for key in thisdict.keys():
    print(key)
print("\n")

# to loop in value 

for value in thisdict.values(): 
    print(value)
print("\n")

# to loop in item  

for key , value in thisdict.items():
    print(key, value)

# ------------------------------
# to copy 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# anthor method

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

