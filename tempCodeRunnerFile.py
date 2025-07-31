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
print(df.iloc[[0]]) # return BR row as DataFrame 
print(df.iloc[[0 , 1]]) # return BR and SA row as DataFrame 


print(df.iloc[1, [2]]) # return area for RU as a series 