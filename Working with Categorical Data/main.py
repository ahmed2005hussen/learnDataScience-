import pandas as pd 
# Take a look of your data 
df = pd.read_csv("adult.csv")

print(df.info()) # From these code you will take a look in what in our data ?
print("\n\n")

print(df["Marital Status"].describe())
print("\n\n")

print(df["Marital Status"].value_counts() )
print("\n\n")

# Relative Frequency : 
print(df["Marital Status"].value_counts(normalize=True) )
print("\n\n")

# -----------------
# Categorical data in pandas

import pandas as pd 
df = pd.read_csv("adult.csv")

print(df["Marital Status"].dtype) # Object 

df["Marital Status"] = df["Marital Status"].astype("category")
print(df["Marital Status"].dtype) # category 


# Creating a categorical Series

import pandas as pd

my_data = ["A", "A", "C", "B", "C", "A"]

my_series1 = pd.Series(my_data,dtype= "category")
print(my_series1)

# OR 

import pandas as pd
my_data = ["A", "A", "C", "B", "C", "A"]
my_series2 = pd.Categorical(my_data , categories=["C" ,"B" , "A"] ,
                            ordered=True)

print(my_series2)


# Why do we use categorical ->  memory

import pandas as pd 
df = pd.read_csv("adult.csv")
print(df["Marital Status"].nbytes)

df["Marital Status"] = df["Marital Status"].astype("category")
print(df["Marital Status"].nbytes) 

# --------------------

# Specify dtypes when reading data 

import pandas as pd 

adult_dtypes = {"Marital Status": "category"}

df = pd.read_csv("adult.csv" , dtype= adult_dtypes)

print(df["Marital Status"].dtype)

# --------------------------

# Grouping data by category in pandas

import pandas as pd 

adult = pd.read_csv("adult.csv" )

gb = adult.groupby(by = ["Sex" , "Above/Below 50k"])

# Print out how many rows are in each created group
print(gb.size())

# ----------------------------

# Setting category variables

import pandas as pd

dogs = pd.DataFrame({
    "name": ["Buddy", "Luna", "Max"],
    "coat": ["short", "long", "medium"]
})

dogs["coat"] = dogs["coat"].astype("category")

print(dogs["coat"].cat.categories)
# Output: ['long', 'medium', 'short']  (ترتيب افتراضي)

# نحدد الترتيب اللي عايزينه
dogs["coat"] = dogs["coat"].cat.set_categories(
    ["short", "medium", "long"]
)

print(dogs["coat"].cat.categories)
# Output: ['short', 'medium', 'long']


# Set Order

dogs["coat"] = dogs["coat"].cat.set_categories(
    ["short", "medium", "long"]
    ,ordered=True
)
print(dogs["coat"].cat.categories)


# ----------------
# Adding categories

import pandas as pd

dogs = pd.DataFrame({
    "name": ["Buddy", "Luna", "Max"],
    "likes_people": ["yes", "no", "yes"]
})

# تحويل العمود لـ category
dogs["likes_people"] = dogs["likes_people"].astype("category")
print(dogs["likes_people"].cat.categories)
# Output: ['no', 'yes']

# إضافة قيم جديدة
dogs["likes_people"] = dogs["likes_people"].cat.add_categories(
    ["did not check", "could not tell"]
)
print(dogs["likes_people"].cat.categories)
# Output: ['no', 'yes', 'did not check', 'could not tell']
print(dogs["likes_people"])

print(dogs["likes_people"].value_counts(dropna=False))

# ----------------------------------
# Removing categories

import pandas as pd

# DataFrame بسيط
dogs = pd.DataFrame({
    "coat": ["short", "long", "wirehaired", "short", "wirehaired"]
})

# نحول العمود إلى category
dogs["coat"] = dogs["coat"].astype("category")

print("📌 Before Delete: ")
print(dogs["coat"].value_counts())
print("Categories:", dogs["coat"].cat.categories)

# نشيل الكاتيجوري "wirehaired"
dogs["coat"] = dogs["coat"].cat.remove_categories(["wirehaired"])

print("\n📌 After Delete: ")
print(dogs["coat"].value_counts())
print("Categories:", dogs["coat"].cat.categories)


# -------------------------

# Methods recap
# Setting: cat.set_categories()
#   - Can be used to set the order of categories
#   - All values not specified in this method are dropped

# Adding: cat.add_categories()
#   - Does not change the value of any data in the DataFrame
#   - Categories not listed in this method are left alone

# Removing: cat.remove_categories()
#   - Values matching categories listed are set to NaN

# -----------------

# Renaming Categories 


import pandas as pd

dogs = pd.DataFrame({
    "breed": ["Labrador", "Unknown Mix", "Poodle", "Unknown Mix"]
})

# نحول العمود لكاتيجوري
dogs["breed"] = dogs["breed"].astype("category")

print("📌 Before:")
print(dogs["breed"].cat.categories)

# نعمل التغيير
my_changes = {"Unknown Mix": "Unknown"}
dogs["breed"] = dogs["breed"].cat.rename_categories(my_changes)

print("\n📌 After:")
print(dogs["breed"].cat.categories)
print(dogs)

# -----------------------------

# Collapsing categories example
import pandas as pd

dogs = pd.DataFrame({
    "color": [
        "black and brown",
        "black and tan",
        "black and white",
        "white",
        "brown",
        "black"
    ]
})

dogs["color"] = dogs["color"].astype("category")
print("Before: ")
print(dogs["color"].cat.categories)

# نعمل قاموس للتحديث (replace)
update_colors = {
    "black and brown": "black",
    "black and tan": "black",
    "black and white": "black",
}

# نعمل عمود جديد بعد التعديل
dogs["main_color"] = dogs["color"].replace(update_colors)

print("\n\n")
print(dogs["main_color"].dtype) # Object
dogs["color"] = dogs["color"].astype("category")

print("\n After")
print(dogs["main_color"].cat.categories)

# ---------------------------------

# Reordring 

import pandas as pd

# DataFrame بسيط
dogs = pd.DataFrame({
    "coat": ["short", "long", "wirehaired", "short", "wirehaired"]
} )
dogs["coat"] = dogs["coat"].astype("category")

dogs['coat'] = dogs["coat"].cat.reorder_categories(
    new_categories = ['short', 'wirehaired', 'long'],  ordered=True)


# OR

dogs["coat"].cat.reorder_categories(
    new_categories = ['short', 'medium', 'wirehaired', 'long'],  ordered=True,  inplace=True)


# ----------------------------------

import pandas as pd

dogs = pd.DataFrame({
    "name": ["Buddy", "Luna", "Max"],
    "coat": ["short", "long", "medium"]
})

dogs["coat"] = dogs["coat"].astype("category")

print(dogs["coat"].cat.categories)
# Output: ['long', 'medium', 'short']  (ترتيب افتراضي)

# نحدد الترتيب اللي عايزينه
dogs["coat"] = dogs["coat"].cat.set_categories(
   new_categories= ["short", "medium", "long"]
)
print(dogs["coat"].cat.categories)

dogs["coat"] = dogs["coat"].cat.remove_categories(removals="short")
print(dogs["coat"].cat.categories)

# --------------------------------------

# Strip away leading whitespace
# dogs["sex"] = dogs["sex"].str.strip()
# dogs["sex"] =  dogs["sex"].str.lower()

# Count the number of dogs that have "English" in their breed name
# print(dogs[dogs["breed"].str.contains("English", regex=False)].shape[0])