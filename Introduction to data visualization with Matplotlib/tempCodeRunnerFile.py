import matplotlib.pyplot as plt
import pandas as pd
medals = pd.read_csv(r"Introduction to data visualization with Matplotlib\olympics_medals.csv",index_col= 0)
fig , ax = plt.subplots()
ax.bar(medals.index , medals["Gold"])
ax.set_xticklabels(medals.index ,rotation = 45)
ax.set_ylabel("Number of medals")
fig.set_size_inches([5,8]) # width , heigth

fig.savefig("gold_medals.jpg") # to save png 