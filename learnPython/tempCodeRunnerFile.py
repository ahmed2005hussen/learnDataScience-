import csv  
with open("test.csv" , "a",newline = "") as f: 
    writer = csv.writer(f)
    writer.writerow(["Hello", 21])
