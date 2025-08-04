# pandas deal with data frame.
# data frame == tables 

# To create Date Frame  
import pandas as pd 
dict = {
    
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}
x = pd.DataFrame(dict) 
print(x)
print("\n \n")
#---------------------------------
# Change index for your data frame, index like primary key in sql  
import pandas as pd 
dict = {
    
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

x = pd.DataFrame(dict) 
x.index = {"BR","RU","IN","CH","SA"} # change index for your data frame
print(x)
print("\n \n")

#---------------------------------
#create csv file to store the data 

import pandas as pd 
dict = {
    
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

df = pd.DataFrame(dict)
df.to_csv("Country.csv")

#---------------------------------

#read form csv file 
import pandas as pd 

df = pd.read_csv("Country.csv")
print(df)
print("\n \n")
#---------------------------------
# Edit index 

#read form csv file 
import pandas as pd 

df = pd.read_csv("Country.csv" , index_col= 0)
print(df)
print("\n \n")

# ------------------------------------

# To access on data
import pandas as pd
dict = {
    
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

df = pd.DataFrame(dict)

print(df["country"]) # return series not data frame 
print("\n \n")

print(df[["country"]]) # return DataFrame 
print("\n \n")

print(df[1:4]) # row 1 , 2 and 3 and their columns 
print("\n \n")

# ------------------------------------
# To access on data using loc  

import pandas as pd
dict = {
    
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

df = pd.DataFrame(dict)
df.index = {"BR","RU","IN","CH","SA"} 



print(df.loc["BR"]) # return BR row as series 
print("\n \n")

print(df.loc[["BR"]]) # return BR row as DataFrame 
print("\n \n")

print(df.loc[["BR" , "SA"]]) # return BR and SA row as DataFrame 
print("\n \n")


print(df.loc['RU' , ["area"]]) # return area for RU as a series 
print("\n \n")

print(df.loc[['RU'] , ["area"]]) # return area for RU as a DataFrame 
print("\n \n")


print(df.loc[:,["country" , "area"]]) # return country and area for all data as DataFrame 
print("\n \n")

print(df.loc[["RU"],:]) # return all column for RU as DataFrame 
print("\n \n")

# -------------------------------------------------------------------
# To access data using iloc
import pandas as pd
dict = {
    
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

df = pd.DataFrame(dict)
df.index = ["BR", "RU", "IN", "CH", "SA"]


print(df.iloc[0]) # return BR row as series 
print("\n \n")

print(df.iloc[[0]]) # return BR row as DataFrame 
print("\n \n")

print(df.iloc[[0 , 1]]) # return BR and SA row as DataFrame 
print("\n \n")


print(df.iloc[1, [2]]) # return area for RU as a series 
print("\n \n")

print(df.iloc[[1] , [2]]) # return area for RU as a DataFrame 
print("\n \n")

# -------------------------------------------------------------------
# compare 
import pandas as pd
import numpy as np
data = pd.read_csv("Country.csv" , index_col=0)

greater = data["area"] > 8
print(data[greater])
print("\n \n")
print(np.logical_and(data["area"] > 8 , data["area"] < 17))
print("\n \n")
print(data[np.logical_and(data["area"] > 8 , data["area"] < 17)])
print("\n")
print(data[(data["area"] > 8) & (data["area"] < 17)])
#--------------------------------------------

# looping 
import pandas as pd
brics = pd.read_csv("Country.csv" , index_col=0)
for lab , row in brics.iterrows():
    print(lab)
    print(row)
    print("----")



import pandas as pd
brics = pd.read_csv("Country.csv" , index_col=0)
for lab , row in brics.iterrows():
    print(str(lab) + " " + row["country"])
        
    print("----")


# create new column in data frame
import pandas as pd
brics = pd.read_csv("Country.csv" , index_col=0)
for lab , row in brics.iterrows():
    brics.loc[lab, "name_length"] = len(row["country"])

print(brics)

# easier method 
import pandas as pd
brics = pd.read_csv("Country.csv" , index_col=0)
brics["name_length"] = brics["country"].apply(len)
print(brics)

# ------------------

# Data Manipulation with pandas : 
# -------------------------------

# if you have a huge data , and want to see just a few rows : 

import pandas as pd 

x = pd.read_csv("First Project\workspace\\netflix_data.csv")
print(x.head(2)) # print the first 2 rows only 
#---------------------------------
import pandas as pd 

x = pd.read_csv("First Project\workspace\\netflix_data.csv")
print(x.shape) # (number of rows , number of columns )

# ------------------------------
# if you want to know : count , mean , std , min , max use describe() method 
# conut is the number of non missing value in your numerical table 
# this method give you fast look in your data 

import pandas as pd 

x = pd.read_csv("First Project\workspace\\netflix_data.csv")
print(x.describe())
# -----------------------

import pandas as pd 

x = pd.read_csv("First Project\workspace\\netflix_data.csv")
print(x.values) # return data in list 
print(x.columns) # name of columns table 
print(x.index)  
# ----------------------------
# Print information about the column types and missing values in 
import pandas as pd 

x = pd.read_csv("First Project\workspace\\netflix_data.csv")
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
print("The mode is : ",data["family_members"].mode()[0])
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
print(notduplicated["color"].value_counts(normalize=True))

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

# values is the column you want to summarize 
# index is the column that you want to group by 
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