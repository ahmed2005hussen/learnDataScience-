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