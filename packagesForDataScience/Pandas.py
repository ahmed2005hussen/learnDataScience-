# Basic 
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
#  change index for your data frame  
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
