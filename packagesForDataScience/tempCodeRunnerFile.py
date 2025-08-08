
import pandas as pd

dic = {
    "name" : ["ahmed" , "hussein" , "mohamed"],
    "age" : [20,10,11],
    "position" : ["developer" , "manager" , "enginner"]
} 

data = pd.DataFrame(dic)
print(data)
print("\n \n")
newdata = data.set_index("name")
print(newdata)

print("\n  \n")
print(newdata.reset_index())

# Dropping an index 
print("\n\n")

print(newdata.reset_index(drop=True))