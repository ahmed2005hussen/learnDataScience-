# read from text file 
fileName = "file.txt"
file = open(fileName , mode= "r" ) # r for reading 
text = file.read()
print(text)
file.close()
# --------------------------------
fileName = "file.txt"
file = open(fileName , mode = "w")
text = file.write("ahmed")
file.close()
#--------------------------
# don't need to close : 
with open("file.txt" , "r")as f : 
    print(f.read())

# -------------------------
# If all data are numbers u can use numpy 

import numpy as np 

fileName = "file.txt"
file = np.loadtxt(fileName , delimiter=',' , skiprows=1)
print(file)

# if you want just first and 3rd col 
import numpy as np 

fileName = "file.txt"
file = np.loadtxt(fileName , delimiter=',' , skiprows=1 , usecols=[0,2])
print(file)

# -------------------

import numpy as np 
import pandas as pd 
fileName = "file.txt"
file = np.loadtxt(fileName , delimiter=',' , dtype="str")
print(file)

# tends to break down if you have mix of data types 

# ------------------------------
# Import the first 5 rows of the file into a DataFrame using the function pd.read_csv() 
# and assign the result to data. You'll need to use the arguments nrows and header.
# Note that there is no header row in this file.


# Build a numpy array from the resulting DataFrame in data and assign to data_array.
# Execute print(type(data_array)) to print the datatype of data_array.


# Read the first 5 rows of the file into a DataFrame: data:

data = pd.read_csv(file, nrows=5, header=None )

# Build a numpy array from the DataFrame: data_array:

data_array = data.to_numpy()


# --------------------

# Key arguments for pd.read_csv() include:

# sep sets the expected delimiter.
# You can use ',' for comma-delimited.
# You can use '\t' for tab-delimited.
# comment takes characters that comments occur after in the file, 
# indicating that any text starting with these characters should be ignored.

# na_values takes a list of strings to identify as NA/NaN. 
# By default, some values are already recognized as NA/NaN. 
# Providing this argument will supply additional values.

data = pd.read_csv(file, sep='\t', comment='#', na_values=["Nothing"])

# Pickled files
# هي ملفات بتتخزن فيها الكائنات في بايثون
# بعد ما تتحول لشكل ثانوي (binary format)

# Idea is : 
# أي حاجة في بايثون (قائمة، قاموس، DataFrame من Pandas، نموذج Machine Learning، إلخ)
#  ممكن تتحول إلى byte stream (سلسلة من البايتات).
# العملية دي اسمها Pickling.
# ولما نحب نسترجع الكائن من الملف، بنعمل Unpickling.


# 📌 ليه نستخدم Pickle

# عشان نحفظ كائن زي ما هو (بكل تفاصيله) بدل ما نخزنه كـ نص أو CSV.
# مفيد جدًا في:

# تخزين النماذج المدربة في Machine Learning.

# حفظ DataFrames كبيرة واستخدامها بعدين.

import pickle

# كائن (dict)
data = {"name": "Ahmed", "age": 20, "skills": ["Python", "ML"]}

# ✅ نحفظ الكائن في ملف Pickle
with open("data.pkl", "wb") as f: # wb -> w to write , b to binary 
    pickle.dump(data, f)

# ✅ نقرأ الكائن تاني من الملف
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)

# ----------------------

# Excel Sheet : 
# dummy example 
import pandas as pd
file = 'urbanpop.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names) 
df1 = data.parse('1960-1966') # sheet name, as a string
df2 = data.parse(0) # sheet index, as a float
