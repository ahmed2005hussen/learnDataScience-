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

# ---------------------------------------------

# Semi Join -> بيجيب لك الصفوف من الجدول الأول اللي ليها تطابق في الجدول التاني،
# لكن ما بيجيبش الأعمدة من الجدول التاني.

import pandas as pd

customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name': ['Ali', 'Sara', 'Omar']
})

orders = pd.DataFrame({
    'order_id': [1001, 1002],
    'customer_id': [1, 3]
})

innerJoin = customers.merge(orders , on = "customer_id" , how = "inner")
semi_join = customers[customers["customer_id"].isin(innerJoin["customer_id"])]
print(semi_join)

# OR

import pandas as pd

customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name': ['Ali', 'Sara', 'Omar']
})

orders = pd.DataFrame({
    'order_id': [1001, 1002],
    'customer_id': [1, 3]
})

semi_join = customers[customers["customer_id"].isin(orders["customer_id"])]
print(semi_join)
# ---------------------------------
# Anti Join -> Returns The Left table, excluding the intersection 
# Returns only columns from the left table not the right 


import pandas as pd

customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name': ['Ali', 'Sara', 'Omar']
})

orders = pd.DataFrame({
    'order_id': [1001, 1002],
    'customer_id': [1, 3]
})

left_join = customers.merge(orders , on = "customer_id" , how = "left" , indicator= True) 
# indicator -> add column named _merge , this column tell us if this row from left or right or both tables 
from_left_only = left_join.loc[left_join["_merge"] == "left_only"]
anti_merge = customers[customers["customer_id"].isin(from_left_only["customer_id"])]
print(anti_merge)

# OR 

import pandas as pd

customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name': ['Ali', 'Sara', 'Omar']
})

orders = pd.DataFrame({
    'order_id': [1001, 1002],
    'customer_id': [1, 3]
})

# Anti join: العملاء اللي ما عندهمش طلبات
anti_join = customers[~customers['customer_id'].isin(orders['customer_id'])]

print(anti_join)

# --------------------------

# Concatenate DataFrames together vertically

import pandas as pd

inv_jan = pd.DataFrame({
    'product': ['A', 'B'],
    'sales': [100, 150]
})

inv_feb = pd.DataFrame({
    'product': ['C', 'D'],
    'sales': [200, 250]
})

inv_mar = pd.DataFrame({
    'product': ['E', 'F'],
    'sales': [300, 350]
})

result = pd.concat([inv_jan , inv_feb ,inv_mar])
print(result)
# look on index we have something wrong
# to solve it use (ignore_index = True)

import pandas as pd

inv_jan = pd.DataFrame({
    'product': ['A', 'B'],
    'sales': [100, 150]
})

inv_feb = pd.DataFrame({
    'product': ['C', 'D'],
    'sales': [200, 250]
})

inv_mar = pd.DataFrame({
    'product': ['E', 'F'],
    'sales': [300, 350]
})

result = pd.concat([inv_jan , inv_feb ,inv_mar] , ignore_index= True)
print(result)

# Setting labels to original tables

import pandas as pd

inv_jan = pd.DataFrame({
    'product': ['A', 'B'],
    'sales': [100, 150]
})

inv_feb = pd.DataFrame({
    'product': ['C', 'D'],
    'sales': [200, 250]
})

inv_mar = pd.DataFrame({
    'product': ['E', 'F'],
    'sales': [300, 350]
})

result = pd.concat([inv_jan , inv_feb ,inv_mar] , ignore_index= False , keys=["Jan" , " Feb" , "Mar"])
print(result)

# you can sort

import pandas as pd

inv_jan = pd.DataFrame({
    'product': ['A', 'B'],
    'sales': [100, 150]
})

inv_feb = pd.DataFrame({
    'product': ['C', 'D'],
    'sales': [200, 250]
})

inv_mar = pd.DataFrame({
    'product': ['E', 'F'],
    'sales': [300, 350]
})

result = pd.concat([inv_jan , inv_feb ] , sort = True)
print(result)


# Join

import pandas as pd

inv_jan = pd.DataFrame({
    'product': ['A', 'B'],
    'sales': [100, 150]
})

inv_feb = pd.DataFrame({
    'product': ['C', 'D'],
    'sales': [200, 250]
})

inv_mar = pd.DataFrame({
    'product': ['E', 'F'],
    'sales': [300, 350]
})

result = pd.concat([inv_jan , inv_feb ] , join= "inner")
print(result)

# ---------------------------

# Verifying integrity

import pandas as pd

customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name': ['Ali', 'Sara', 'Omar']
})

orders = pd.DataFrame({
    'order_id': [1001, 1002],
    'customer_id': [1, 1]
})

# result = customers.merge(orders , on = "customer_id" , how = "inner" , validate= "one_to_one")
# Error because it is not one to one relation

result = customers.merge(orders , on = "customer_id" , how = "inner" , validate= "one_to_many")
print(result)

# ----------------------------------

import pandas as pd

customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name': ['Ali', 'Sara', 'Omar']
})

orders = pd.DataFrame({
    'order_id': [1001, 1002],
    'customer_id': [1, 1]
})

# result = pd.concat([customers,orders] , verify_integrity= True) # check if we have duplicate 
# Error because it is not one to one relation

result = pd.concat([customers,orders] , verify_integrity = False)
print(result)

# ---------------