# Joning Data -> you have multiple table and you want data from them 
# To do this you want to join your tables
 
# Tables = DataFrames 
# Merging = Joining 

# Inner Join -> هيرجع المشترك بين الاتنين
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

# ---------------------------
# Left Join -> هيرجع اللي في الشمال كله و لو في حاجه من اليمين موجوده في الشمال 

import pandas as pd
students = pd.read_csv(r"Joining Data With Pandas\students.csv")
grades = pd.read_csv(r"Joining Data With Pandas\grades.csv")

left_join = students.merge(grades , on = "StudentID"  , how = "left")
print(left_join)

# Right Join -> عكس ال left

import pandas as pd
students = pd.read_csv(r"Joining Data With Pandas\students.csv")
grades = pd.read_csv(r"Joining Data With Pandas\grades.csv")

right_join = students.merge(grades , on = "StudentID"  , how = "right")
print(right_join)

# outer join هيرجع كله اليمين و الشمال

import pandas as pd
students = pd.read_csv(r"Joining Data With Pandas\students.csv")
grades = pd.read_csv(r"Joining Data With Pandas\grades.csv")

outer_join = students.merge(grades , on = "StudentID"  , how = "outer")
print(outer_join)

# if the name of "on columns" different u can use 

# table1.merge(table2 , left_on = nameColumn , right_on = nameColumn )

# ----------------------------
# self join 
# Self Join is when a table is joined with itself.

# It’s used when you need to relate rows within the same table 
# based on a condition.

# table.merge(table , left_on = namecol , right_on = nameCol)

# -----------------------------
# Merging on index يعني هنخلي عمود هو الاندكس بعد ال merge

# table1.merge(table2 , left_on = namecol , right_on = nameCol , right_index = True)
