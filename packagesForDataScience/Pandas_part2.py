# Data Manipulation with pandas : 
# -------------------------------

# if you have a huge data , and want to see just a few rows : 

import pandas as pd 

x = pd.read_csv(r"projects\Netflix project\workspace\netflix_data.csv")
print(x.head(2)) # print the first 2 rows only 
#---------------------------------
import pandas as pd 

x = pd.read_csv(r"projects\Netflix project\workspace\netflix_data.csv")
print(x.shape) # (number of rows , number of columns )

# ------------------------------
# if you want to know : count , mean , std , min , max use describe() method 
# conut is the number of non missing value in your numerical table 
# this method give you fast look in your data 

import pandas as pd 

x = pd.read_csv(r"projects\Netflix project\workspace\netflix_data.csv")
print(x.describe())
# -----------------------

import pandas as pd 

x = pd.read_csv(r"projects\Netflix project\workspace\netflix_data.csv")
print(x.values) # return data in list 
print(x.columns) # name of columns table 
print(x.index)  
# ----------------------------
# Print information about the column types and missing values in 
import pandas as pd 

x = pd.read_csv(r"projects\Netflix project\workspace\netflix_data.csv")
print(x.info())
# ---------------------------
# sort by column value acsending 
import pandas as pd 
x = pd.read_csv("data manipulation with pandas\homelessness.csv")
print(x.head(4))
print("\n")
x = x.sort_values("family_members")
print(x.head(4))

# sort by column value descending 

import pandas as pd 
x = pd.read_csv("data manipulation with pandas\homelessness.csv")
print(x.head(4))
print("\n")
x = x.sort_values("family_members",ascending=False)
print(x.head(4))

# sort by more than one column 

import pandas as pd 
x = pd.read_csv("data manipulation with pandas\homelessness.csv")
print(x.head(4))
print("\n")
x = x.sort_values(["family_members" , "state_pop"])
print(x.head(4))

import pandas as pd 
x = pd.read_csv("data manipulation with pandas\homelessness.csv")
print(x.head(4))
print("\n")
x = x.sort_values(["family_members" , "state_pop"] , ascending= [True,False])
print(x.head(4))

# ---------------
# subsetting

import pandas as pd 
x = pd.read_csv("data manipulation with pandas\homelessness.csv")
MountainRegion = x[x["region"].isin(["Mountain"])]
print(MountainRegion) # give all Mountain regiion 
#----------------------------------
# summary statistics 

import pandas as pd 

data = pd.read_csv("data manipulation with pandas\homelessness.csv")

print("The mean is : ",data["family_members"].mean())
print("The meadian is : ",data["family_members"].median())
print("The mode is : ",data["family_members"].mode()[0]) # as we may have multiple modes 
print("The min is : ",data["family_members"].min())
print("The max is : ",data["family_members"].max())
print("The std is : ",data["family_members"].std())
print("The var is : ",data["family_members"].var())
print("The sum is : ",data["family_members"].sum())
print("The quantile is : ",data["family_members"].quantile(0.3)) # 30%


def fun(column):
    return column.quantile(0.3)

print(data["family_members"].agg(fun))


print("cumulative sum is : " , data["family_members"].cumsum())
print("cumulative min is : " , data["family_members"].cummin())
print("cumulative max is : " , data["family_members"].cummax())
print("cumulative product is : " , data["family_members"].cumprod())

# -----------------------------------------------------

# to avoid duplicate names 

import pandas as pd
dic = {
    "name" : ["ahmed", "hussein" , "nada" , "ahmed" , "mohammed", "ahmed"]
    ,"age" : [21 , 58 , 19 , 20 , 20 , 20],
    "color" : ["red" , "blue" , "blue" , "white" , "blue" ,"green"]
}

data = pd.DataFrame(dic)
notduplicated = data.drop_duplicates(subset="name")
print(notduplicated)
print(notduplicated["color"].value_counts())
print(notduplicated["color"].value_counts(normalize=True)) # هيقسم كل قيمة على إجمالي عدد العناصر ويطلعلك النسبة

print("\n")


notduplicated = data.drop_duplicates(subset=["name","age"])
print(notduplicated)
print(notduplicated["color"].value_counts(sort=True)) # count and sort decs
print(notduplicated["color"].value_counts(normalize=True)) # count and give the precentage 


# --------------------------

import pandas as pd 

data = pd.read_csv("data manipulation with pandas\sales_subset.csv")

groupBy = data.groupby("store")["temperature_c"].agg([sum,min,max])
print(groupBy)

groupBy = data.groupby(["store","department"])["temperature_c"].mean()
print("\n")
print(groupBy)

# --------------------
#  pivot table 
# like group by 

import pandas as pd
data = pd.read_csv("data manipulation with pandas\sales_subset.csv")

# values : is the column you want to summarize 
# index : is the column that you want to group by 
# by default, pivot table takes the mean value for each group 

groupBy = data.pivot_table(values="temperature_c",index="store")
print(groupBy)

# if you want more than one statictic use aggfun()

import pandas as pd
data = pd.read_csv("data manipulation with pandas\sales_subset.csv")

groupBy = data.pivot_table(values="temperature_c",index="store" , aggfunc=["median" , "mean"])
print(groupBy)
# group by more than one column 
groupBy = data.pivot_table(values="temperature_c",index="store" , columns="department", aggfunc=["median" , "mean"])
print(groupBy)
# to filter missing value 
groupBy = data.pivot_table(values="temperature_c",index="store" , columns="department", aggfunc=["median" , "mean"] , fill_value=0)
print(groupBy)

# الصف All: بيمثل المتوسط أو المجموع الكلي لكل الأعمدة (يعني المتوسط/المجموع عبر كل الـ stores).
# العمود All: بيمثل المتوسط/المجموع لكل الصفوف (يعني عبر كل الـ departments).
groupBy = data.pivot_table(values="temperature_c",index="store" , columns="department", aggfunc=["median" , "mean"] , fill_value=0 , margins=True)
print(groupBy)

# ----------------------------------
# Slicing and Indexing DataFrames


import pandas as pd

dic = {
    "name" : ["ahmed" , "hussein" , "mohamed"],
    "age" : [20,10,11],
    "position" : ["developer" , "manager" , "enginner"]
} 

data = pd.DataFrame(dic)
print(data)
print("\n \n")
newdata = data.set_index("name")
print(newdata)

print("\n  \n")
print(newdata.reset_index())

# Dropping an index 
print("\n\n")

print(newdata.reset_index(drop=True))
# ---------------------------------------

# missing value 

import pandas as pd 
import numpy as np
data = {
    "Name": ["Ali", "Sara", "Omar", "Mona", None],
    "Age": [25, None, 30, 22, 28],
    "City": ["Cairo", "Alexandria", None, "Giza", "Cairo"],
    "Salary": [5000, 7000, np.nan, 4500, 6000]
}

df = pd.DataFrame(data)

print(df.isna())
print("\n \n")
print(df.isna().any()) # detecting any missing value in columns 
print("\n\n")
print(df.isna().sum())

# remove missing values
# method one delete rows which contain missing value 
print("\n\n")
m1 = df.dropna()
print(m1)
print('\n\n')
# method 2 replace with 0 
m2 = df.fillna(0)
print(m2)