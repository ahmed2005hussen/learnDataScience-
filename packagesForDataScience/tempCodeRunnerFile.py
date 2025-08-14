
import pandas as pd
students = pd.read_csv(r"Joining Data With Pandas\students.csv")
grades = pd.read_csv(r"Joining Data With Pandas\grades.csv")

outer_join = students.merge(grades , on = "StudentID"  , how = "outer")
print(outer_join)