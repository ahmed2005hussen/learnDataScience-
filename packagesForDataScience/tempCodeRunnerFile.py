import pandas as pd
brics = pd.read_csv("Country.csv" , index_col=0)
for lab , row in brics.iterrows():
    print(lab) # -> index 
    print(row)
    print("----")