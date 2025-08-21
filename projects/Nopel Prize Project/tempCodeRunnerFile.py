import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"Nopel Prize Project\data\nobel.csv")

print(df.columns)
# What is the most commonly awarded gender and birth country?
# Store your answers as string variables top_gender and top_country.



sns.catplot(kind = "count" , x = "sex" , hue="sex", data = df)
plt.show()