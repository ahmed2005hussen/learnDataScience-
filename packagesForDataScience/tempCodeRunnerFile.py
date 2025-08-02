import pandas as pd
import numpy as np
data = pd.read_csv("Country.csv" , index_col=0)

greater = data["area"] > 8
print(data[greater])
print("\n \n")
print(np.logical_and(data["area"] > 8 , data["area"] < 17))
print("\n \n")
print(data[np.logical_and(data["area"] > 8 , data["area"] < 17)])