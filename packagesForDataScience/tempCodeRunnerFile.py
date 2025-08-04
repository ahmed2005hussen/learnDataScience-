import pandas as pd 
x = pd.read_csv("data manipulation with pandas\homelessness.csv")
MountainRegion = x[x["region"].isin(["Mountain"])]
print(MountainRegion)