import pandas as pd
df = pd.read_csv("employee_salaries_original.csv")

print(df["experience_level"].nunique())

check = df["experience_level"].str.contains("ior")
print(df[check])