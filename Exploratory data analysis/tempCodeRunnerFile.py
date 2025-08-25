
import pandas as pd

planes = pd.DataFrame({
    "Price": [100, 200, 300, 400, 500, 600, 1000, 2000]
})


twenty_fifth = planes["Price"].quantile(0.25)
median = planes["Price"].median()
seventy_fifth = planes["Price"].quantile(0.75)
maximum = planes["Price"].max()

labels = ["Economy", "Premium Economy", "Business Class", "First Class"]
bins = [0, twenty_fifth, median, seventy_fifth, maximum]

planes["Price_Category"] = pd.cut(planes["Price"],labels=labels, bins=bins)
print(planes)