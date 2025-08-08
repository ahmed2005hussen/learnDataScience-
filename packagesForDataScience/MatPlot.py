import matplotlib.pyplot as plt
import pandas as pd 

date = [1950 , 1970 , 1990 , 2010]
salary = [2.519, 3.692,5.263,6.972]

# Type of plots 

# Line Bar 

# plt.plot(x-axis , y-axis)
plt.plot(date,salary)
plt.show()

# ------------------

# scatter 
import matplotlib.pyplot as plt 
date = [1950 , 1970 , 1990 , 2010]
salary = [2.519, 3.692,5.263,6.972]

# plt.scatter(x-axis , y-axis)

plt.scatter(date , salary)
plt.show()

# ----------------

# vertical bar chart 

import matplotlib.pyplot as plt 
date = [1950 , 1970 , 1990 , 2010]
salary = [2.519, 3.692,5.263,6.972]

# plt.bar(x-axis , y-axis)

plt.bar(date,salary)
plt.show()
#--------------------
# Horizantil bar chart

import matplotlib.pyplot as plt 
date = [1950 , 1970 , 1990 , 2010]
salary = [2.519, 3.692,5.263,6.972]

# plt.barh(y-axis , x-axis)

plt.barh(date,salary)
plt.show()

# -----------------------
# Histogram

import matplotlib.pyplot as plt 
date = [74,83,69,95,78,85,42,98,73,68,90,85,84,71,88,52,94]
# bins like group 
plt.hist(date,bins=6)
plt.show()

# --------------------
# pie chart

# plt.pie(values القيم اللي عايز تحطها ,
#  Labels اسماء كل قطعه من الدايره , autopct  لاظهار النسبه المئويه)

import matplotlib.pyplot as plt 
degrees = [90 , 95 , 80 , 60 , 70]
Labels =  ["Nada" , "Ahmed" , "Hussein" , "Amr" , "ziad"]
plt.pie(degrees , labels= Labels , autopct='%1.1f%%')
plt.show()
#--------------

# Customization التخصيص 


# make grid 
import matplotlib.pyplot as plt 

date = [1950 , 1970 , 1990 , 2010]
salary = [2.519, 3.692,5.263,6.972]
plt.grid(True)
plt.plot(date,salary)
plt.show()

#-----------------------

# change scales on x or y axis

# on x-axis
import matplotlib.pyplot as plt 

date = [1950 , 1970 , 1990 , 2010]
salary = [2.519, 3.692,5.263,6.972]

plt.xscale("log")
plt.plot(date,salary)
plt.show()


# on y-axis
import matplotlib.pyplot as plt 

date = [1950 , 1970 , 1990 , 2010]
salary = [2.519, 3.692,5.263,6.972]

plt.yscale("log")
plt.plot(date,salary)
plt.show()

# change your limit 

# on x-axis
import matplotlib.pyplot as plt 

date = [1950 , 1970 , 1990 , 2010]
salary = [2.519, 3.692,5.263,6.972]

plt.xlim(0,10000)
plt.plot(date,salary)
plt.show()

# if you want to put strings in y-axis


import matplotlib.pyplot as plt 

date = [1950 , 1970 , 1990 , 2010]
salary = [2.519, 3.692,5.263,6.972]

plt.yticks(salary, ["a" , "b" , "c" ,"d"])
plt.plot(date,salary)
plt.show()
# ----------------

import matplotlib.pyplot as plt 

date = [1950 , 1970 , 1990 , 2010]
salary = [2.519, 3.692,5.263,6.972]

plt.plot(date,salary,alpha = 0.1) # شفافيه
plt.show()

# --------------------------------------
# with pandas 

import pandas as pd 
import matplotlib.pyplot as plt
date = pd.read_csv("Country.csv")
print(date)

# first we will group by country
print("\n\n")
pop = date.groupby("country" , as_index=False)["population"].mean() 
print(pop)

# hist 
pop.hist()
plt.show()


# bar plot
pop.plot(kind="bar")
plt.show()
# line 

pop.plot(
    x= "country",
    y = "population",
    kind="line"
)
plt.show()
#----------------
# to rotaing x-axis 

pop.plot(
    x= "country",
    y = "population",
    kind="line",
    rot=45
)
plt.show()

# scatter

pop.plot(
    x= "country",
    y = "population",
    kind="scatter",
  
)
plt.show()

