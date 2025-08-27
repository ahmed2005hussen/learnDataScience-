import pandas as pd

# DataFrame بسيط
dogs = pd.DataFrame({
    "coat": ["short", "long", "wirehaired", "short", "wirehaired"]
} )
dogs["coat"] = dogs["coat"].astype("category")

print(dogs, "\n\n")
dogs['coat'] = dogs["coat"].cat.reorder_categories(
    new_categories = ['short', 'wirehaired', 'long'],  ordered=True)


print(dogs)