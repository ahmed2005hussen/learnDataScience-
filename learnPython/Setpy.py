# ------------------------------------------
# Author: Ahmed Hussein Ahmed
# ------------------------------------------

# ✅ What is a Set?
# - Unordered, unindexed, and unchangeable collection.
# - Allows only unique items (no duplicates).
# - Mutable (you can add/remove elements).

# ✅ Creating Sets
# - Use curly braces `{}` or the `set()` constructor.

# ✅ No indexing (no access via index like lists).

# ✅ Set Characteristics
# - Duplicates are automatically removed.
# - `True` is treated as 1 → won't appear twice with 1.

# ✅ Set Length & Type
# - Use `len(set)` and `type(set)`.

# ✅ Iteration & Membership
# - Loop using `for item in set`.
# - Use `"item" in set` and `"item" not in set`.

# ✅ Add Elements
# - `.add(item)` to add a single element.
# - `.update(iterable)` to add multiple from list, set, tuple...

# ✅ Remove Elements
# - `.remove(item)` → raises error if item not found.
# - `.discard(item)` → no error if item not found.
# - `.pop()` → removes a random item.
# - `.clear()` → empties the set.
# - `del` → deletes the entire set object.

# ✅ Set Operations

# 🔹 Union (combine elements from both)
#   - `s1.union(s2)` or `s1 | s2`

# 🔹 Intersection (common elements)
#   - `s1.intersection(s2)` or `s1 & s2`
#   - `s1.intersection_update(s2)` → updates s1 directly

# 🔹 Difference (items in s1 but not in s2)
#   - `s1.difference(s2)` or `s1 - s2`
#   - `s1.difference_update(s2)` → updates s1 directly

# 🔹 Symmetric Difference (items not common)
#   - `s1.symmetric_difference(s2)` or `s1 ^ s2`
#   - `s1.symmetric_difference_update(s2)` → updates s1 directly




# A set is a collection which is unordered, unchangeable, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.

thisSet = {1,2,3,8,4}
# print(thisSet[1]) Error 

#Sets are unordered, so you cannot be sure in which order the items will appear.
print(thisSet)

# ----------------------
# not allow duplicate values.

thisSet = {1,1,1,2,3,4}
print(thisSet)

thisSet = {True , 1 , "ahmed"}
print(thisSet)

thisSet = {1, True , "ahmed"}
print(thisSet)

# -------------------

thisSet = {1,2,3,4,4,5}
print(len(thisSet))
print(type(thisSet))

# ----------------------------
# constructor 

thisSet = set((1,2,2,3,4))
print(thisSet)

# access items 

thisSet = {"ahmed", "hussein" , 1 , 2, 3}

for i in thisSet: 
    print(i)

# -------------------

thisSet = {"ahmed", "hussein" , 1 , 2, 3}
print("ahmed" in thisSet)

thisSet = {"ahmed", "hussein" , 1 , 2, 3}
print("ahmed" not in thisSet)

# add items to set 

thisSet = {1,2,3,4}
thisSet.add(5)
print(thisSet)

#  add sets 

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
# ------------------------------

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# If the item to remove does not exist, remove() will raise an error.

thisset = {"apple",  "cherry"}

# thisset.remove("banana") # error

print(thisset)
# -----------------------
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "cherry"}

thisset.discard("banana")

print(thisset)
# remove random element 

thisset = {"apple", "banana", "cherry"}

thisset.pop()

print(thisset)

# clear 
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
# ----------------------
# del
thisset = {"apple", "banana", "cherry"}

del thisset

# print(thisset) Error

# -------------------------------

# union 

s1 = {1,2,3}
s2 = {"ahmed", "hussein",1}
s3 = s1.union(s2)
print(s3)

# or you can use


s1 = {1,2,3}
s2 = {"ahmed", "hussein",1}
s3 = s1 | s2 
print(s3)

# -------------------
# intersection

s1 = {1,2,3,4}
s2 = {2,3,4,5,6,7}
s3 = s1.intersection(s2)
print(s3)

# OR 

s1 = {1,2,3,4}
s2 = {2,3,4,5,6,7}
s3 = s1 & s2
print(s3)

# Keep the items that exist in both set1, and set2
s1 = {1,2,3,4}
s2 = {2,3,4,5,6,7}
s1.intersection_update(s2)
print(s1)
# ------------------
# Difference 

s1 = {1,2,3,4}
s2 = {2,3,4,5,6,7}
s3 = s1.difference(s2)
print(s3)

# or 


s1 = {1,2,3,4}
s2 = {2,3,4,5,6,7}
s3 = s1 - s2
print(s3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
# --------------------

# Keep the items that are not present in both sets

s1 = {1,2,3,4}
s2 = {2,3,4,5,6,7}
s3 = s1.symmetric_difference(s2)
print(s3)
# or 

s1 = {1,2,3,4}
s2 = {2,3,4,5,6,7}
s3 = s1 ^ s2
print(s3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)