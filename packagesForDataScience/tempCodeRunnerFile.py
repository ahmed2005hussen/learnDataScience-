import pandas as pd 

jan = pd.read_csv(r"Joining Data With Pandas\sales_jan.csv")

print(jan['ProductName'].value_counts())