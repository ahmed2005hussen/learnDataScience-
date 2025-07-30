import pandas as pd
dict = {
    
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

df = pd.DataFrame(dict)
df.index = {"BR","RU","IN","CH","SA"} 



# print(df.loc["BR"]) # return BR row as series 
# print(df.loc[["BR"]]) # return BR row as DataFrame 
# print(df.loc[["BR" , "SA"]]) # return BR and SA row as DataFrame 


# print(df.loc['RU' , ["area"]]) # return area for RU as a series 
# print(df.loc[['RU'] , ["area"]]) # return area for RU as a DataFrame 


# print(df.loc[:,["country" , "area"]]) # return country and area for all data as DataFrame 
print(df.loc[["RU"],:]) # return country and area for all data as DataFrame 