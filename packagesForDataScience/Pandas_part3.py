# Joning Data -> you have multiple table and you want data from them 
# To do this you want to join your tables
 
# Tables = DataFrames 
# Merging = Joining 

# Inner Join
import pandas as pd 
feb = pd.read_csv(r"Joining Data With Pandas\sales_feb.csv")
jan = pd.read_csv(r"Joining Data With Pandas\sales_jan.csv")

joining_Data = feb.merge(jan, on = "ProductID" )

print(joining_Data)
# If you look at the output,
# you will notice that the column names have changed
# because the two tables have columns with the same name. 
# Therefore, you will see Price_x and Price_y 
# to differentiate between the two tables.


import pandas as pd 
feb = pd.read_csv(r"Joining Data With Pandas\sales_feb.csv")
jan = pd.read_csv(r"Joining Data With Pandas\sales_jan.csv")

joining_Data = feb.merge(jan, on = "ProductID" , suffixes=("_Feb" , "_Jan" ) )

print(joining_Data)

# Here, we replace the default _x and _y suffixes
# with custom words that have a more meaningful description for us.

# -----------------------------------------
import pandas as pd 

jan = pd.read_csv(r"Joining Data With Pandas\sales_jan.csv")

# كل عنصر ظهر كام مره
print(jan['ProductName'].value_counts())

# ------------------------------------

# To merge Three tables

# table1.merge(table2 , on = [col1,col2,..]).merge(table3,on = col1)