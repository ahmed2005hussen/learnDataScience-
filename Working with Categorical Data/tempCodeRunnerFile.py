import pandas as pd

dogs = pd.DataFrame({
    "name": ["Buddy", "Luna", "Max"],
    "coat": ["short", "long", "medium"]
})

dogs["coat"] = dogs["coat"].astype("category")

print(dogs["coat"].cat.categories)
# Output: ['long', 'medium', 'short']  (ترتيب افتراضي)

# نحدد الترتيب اللي عايزينه
dogs["coat"] = dogs["coat"].cat.set_categories(
   new_categories= ["short", "medium", "long"]
)
print(dogs["coat"].cat.categories)

dogs["coat"] = dogs["coat"].cat.remove_categories(removals="short")
print(dogs["coat"].cat.categories)
