# Joning Data -> you have multiple table and you want data from them 
# To do this you want to join your tables
 
# Tables = DataFrames 
# Merging = Joining 

# Inner Join -> هيرجع المشترك بين الاتنين -> Default 
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

# ---------------------

# Merge_ordered() -> outer join is default 
# use it when u work on ordered data / time series 
import pandas as pd

stock_a = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-03', '2023-01-04'],
    'price_a': [100, 102, 103]
})

stock_b = pd.DataFrame({
    'date': ['2023-01-02', '2023-01-03', '2023-01-05'],
    'price_b': [200, 202, 205]
})

merged = pd.merge_ordered(stock_a, stock_b, on='date')

print(merged)

# filling missing value with previous value

import pandas as pd

stock_a = pd.DataFrame({
    'date': ['2023-01-01', '2023-01-03', '2023-01-04'],
    'price_a': [100, 102, 103]
})

stock_b = pd.DataFrame({
    'date': ['2023-01-02', '2023-01-03', '2023-01-05'],
    'price_b': [200, 202, 205]
})

merged = pd.merge_ordered(stock_a, stock_b, on='date' , fill_method= "ffill")

print(merged)

# -------------------------------
# Using merge_asof()

# هي زي -> left join 
#لكن مش بتعمل المطابقة بالقيمة نفسها
# بتختار أقرب قيمة سابقة أو مساوية في العمود اللي بنعمل عليه الدمج.


# Left Table                # Right Table

# | B  | C  |               | C | D  |
# | -- | -- |               | - | -- |
# | B2 | 1  | - - - - - - ->| 1 | D1 |
# | B3 | 5  | - - -         | 2 | D2 |
# | B4 | 10 | - -  | - - - >| 3 | D3 |  
#                |          | 6 | D6 |
#                | - - - - >| 7 | D7 |


#  Result
 
# | B  | C  | D  |
# | -- | -- | -- |
# | B2 | 1  | D1 |
# | B3 | 5  | D3 |
# | B4 | 10 | D7 |


#  شروط merge_asof():

# لازم العمود اللي بتعمل عليه الدمج  يكون مرتب تصاعديًا.

# بيشتغل زي -> merge_ordered() left join
#  لكن بالمطابقة الأقرب بدل المطابقة الدقيقة.

# مفيد جدًا في دمج البيانات الزمنية - > (time series)
# مثلاً تربط أسعار الأسهم بأقرب تاريخ متاح.


import pandas as pd

left = pd.DataFrame({
    'B': ['B2', 'B3', 'B4'],
    'C': [1, 5, 10]
})

right = pd.DataFrame({
    'C': [1, 2, 3, 6, 7],
    'D': ['D1', 'D2', 'D3', 'D6', 'D7']
})

left = left.sort_values('C')
right = right.sort_values('C')

result = pd.merge_asof(left, right, on='C', direction='backward')
# direction='forward' → هيجيب أقرب قيمة أكبر أو مساوية.
# direction='nearest' → هيجيب أقرب قيمة سواء أصغر أو أكبر حسب المسافة.
# direction='backward' → هيجيب أقرب قيمة أصغر أو مساوية.

print(result)

# ----------------------------

import pandas as pd

data = {
    "Name": ["Ahmed", "Sara", "Omar", "Laila", "Mona"],
    "Age": [23, 30, 19, 25, 28],
    "City": ["Cairo", "Giza", "Cairo", "Alexandria", "Giza"]
}
df = pd.DataFrame(data)

result1 = df.query("Name == 'Ahmed'")
print(result1)

result1 = df.query("Age == 30")
print(result1)

result1 = df.query("Age < 30 and City ==  'Giza' ")
print(result1)

# -------------------------------

# Reshaping data with .melt()


# .melt() in Pandas is used to reshape your DataFrame from a wide format
# to a long format.

# Wide format → each variable has its own column.

# Long format → all variable values are stacked in a single column,
# with another column indicating which variable they came from.

# It’s very useful for data cleaning and preparing your dataset for analysis
# or visualization.

# Before .melt()

# | Name | Math | Science | English |
# | ---- | ---- | ------- | ------- |
# | Ali  | 90   | 85      | 88      |
# | Sara | 78   | 92      | 80      |
# | Omar | 85   | 89      | 94      |

# After .melt()

# | Name | Subject | Score |
# | ---- | ------- | ----- |
# | Ali  | Math    | 90    |
# | Sara | Math    | 78    |
# | Omar | Math    | 85    |
# |------|---------|-------|
# | Ali  | Science | 85    |
# | Sara | Science | 92    |
# | Omar | Science | 89    |
# |------|---------|-------|
# | Ali  | English | 88    |
# | Sara | English | 80    |
# | Omar | English | 94    |


import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'Omar'],
    'Math': [90, 78, 85],
    'Science': [85, 92, 89],
    'English': [88, 80, 94]
}

df = pd.DataFrame(data)
print("📊 قبل melt:")
print(df)
print("\n\n")


# id_vars -> الأعمدة اللي هتفضل زي ما هي
# value_vars -> الأعمدة اللي هتحولها لصفوف
# var_name -> اسم العمود الجديد اللي هيحتوي أسماء الأعمدة القديمة
# value_name ->  اسم العمود الجديد اللي هيحتوي القيم

df_melted = pd.melt(df, id_vars=['Name'], 
                    value_vars=['Math', 'Science', 'English'], 
                    var_name='Subject', 
                    value_name='Score')

print("\n📉 بعد melt:")
print(df_melted)
