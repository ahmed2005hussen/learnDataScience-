# read from csv file 

import csv 

with open("Country.csv" , "r") as f :
    reader = csv.reader(f) # list each index has one row 
    for row in reader : 
        print(row)

# ----------------------------
# write to csv file 

import csv 

with open("test.csv" , "w",newline = "") as f: 
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"]) 
    writer.writerow(["Ahmed", 21])

# --------------------
# add to csv file 

import csv  
with open("test.csv" , "a",newline = "") as f: 
    writer = csv.writer(f)
    writer.writerow(["Hello", 21])

# THX :)