# لو عندنا داتا كبيره جدا 
# ممكن المساحه متسمحش اننا نحملها كلها و نتعامل معاها في نفس الوقت
# الحل هو ال chunksize 

import pandas as pd
for chunk in pd.read_csv(r"projects\Netflix project\workspace\netflix_data.csv" ,
                         chunksize=10):
    print(chunk["show_id"])
    print("Done\n\n")


print("\n\n")

df = pd.read_csv(r"projects\Netflix project\workspace\netflix_data.csv" ,
                         chunksize=10)

print(next(df) ) # first Chunk
print(next(df)) # second chunk 