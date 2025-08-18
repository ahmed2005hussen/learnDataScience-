# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
plt.show()

# ---------------------------

import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.DataFrame({
    "MONTH": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "MLY-PRCP-NORMAL": [145, 110, 120, 80, 60, 40,
                        20, 25, 50, 110, 160, 180]
})

fig , ax = plt.subplots()

ax.plot(seattle_weather["MONTH"]  , seattle_weather["MLY-PRCP-NORMAL"] , 
        marker = "o")
plt.show()

# Or

import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.DataFrame({
    "MONTH": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "MLY-PRCP-NORMAL": [145, 110, 120, 80, 60, 40,
                        20, 25, 50, 110, 160, 180]
})

fig , ax = plt.subplots()

ax.plot(seattle_weather["MONTH"]  , seattle_weather["MLY-PRCP-NORMAL"] , 
        marker = "v")
plt.show()

##################################

import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.DataFrame({
    "MONTH": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "MLY-PRCP-NORMAL": [145, 110, 120, 80, 60, 40,
                        20, 25, 50, 110, 160, 180]
})

fig , ax = plt.subplots()

ax.plot(seattle_weather["MONTH"]  , seattle_weather["MLY-PRCP-NORMAL"] , 
        marker = "v",
        linestyle = "--")
plt.show()

# OR

import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.DataFrame({
    "MONTH": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "MLY-PRCP-NORMAL": [145, 110, 120, 80, 60, 40,
                        20, 25, 50, 110, 160, 180]
})

fig , ax = plt.subplots()

ax.plot(seattle_weather["MONTH"]  , seattle_weather["MLY-PRCP-NORMAL"] , 
        marker = "v",
        linestyle = "None")
plt.show()

# -----------------------------------

import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.DataFrame({
    "MONTH": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "MLY-PRCP-NORMAL": [145, 110, 120, 80, 60, 40,
                        20, 25, 50, 110, 160, 180]
})

fig , ax = plt.subplots()

ax.plot(seattle_weather["MONTH"]  , seattle_weather["MLY-PRCP-NORMAL"] , 
        marker = "v",
        linestyle = "--",
        color = "r")
plt.show()

# --------------------------

import pandas as pd
import matplotlib.pyplot as plt

seattle_weather = pd.DataFrame({
    "MONTH": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "MLY-PRCP-NORMAL": [145, 110, 120, 80, 60, 40,
                        20, 25, 50, 110, 160, 180]
})

fig , ax = plt.subplots()

ax.plot(seattle_weather["MONTH"]  , seattle_weather["MLY-PRCP-NORMAL"] , 
        marker = "v",
        linestyle = "--",
        color = "r")

ax.set_xlabel("Time (month)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
ax.set_title("Weather in seattle ")
plt.show()


# ----------------------------------
#  لو عايز تحط بيانات كتير علي الرسمه و تقارن بينهم 
# لو حطيتهم علي نفس الرسمه الحوار هيبقي عشوائي و مش هتفهم اي حاجه 
# علشان كده بنقسهم رسمتنا لكذا جزء و هنتعامل معاه

import matplotlib.pyplot as plt 

fig, ax = plt.subplots(3,2) # 3 rows , 2 col
plt.show()
print(ax.shape)



# ------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

seattle_weather = pd.DataFrame({
    "MONTH": months,
    "MLY-PRCP-NORMAL": [145, 110, 120, 80, 60, 40, 20, 25, 50, 110, 160, 180],
    "MLY-PRCP-25PCTL": [100, 80, 90, 60, 40, 20, 10, 15, 30, 80, 120, 130],
    "MLY-PRCP-75PCTL": [190, 150, 160, 110, 80, 60, 40, 50, 70, 150, 200, 220]
})

austin_weather = pd.DataFrame({
    "MONTH": months,
    "MLY-PRCP-NORMAL": [60, 55, 70, 80, 90, 100, 95, 85, 80, 70, 65, 60],
    "MLY-PRCP-25PCTL": [40, 35, 50, 60, 70, 80, 75, 65, 60, 55, 50, 45],
    "MLY-PRCP-75PCTL": [80, 75, 90, 100, 110, 120, 115, 105, 100, 85, 80, 75]
})

fig, ax = plt.subplots(2, 1)

ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], linestyle='--', color='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], linestyle='--', color='b')
ax[0].set_ylabel("Precipitation (inches)")

ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], linestyle='--', color='r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], linestyle='--', color='r')
ax[1].set_ylabel("Precipitation (inches)")
ax[1].set_xlabel("Time (months)")

plt.show()

# if you see y axis is not same in to plots 
# to fix it 


import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

seattle_weather = pd.DataFrame({
    "MONTH": months,
    "MLY-PRCP-NORMAL": [145, 110, 120, 80, 60, 40, 20, 25, 50, 110, 160, 180],
    "MLY-PRCP-25PCTL": [100, 80, 90, 60, 40, 20, 10, 15, 30, 80, 120, 130],
    "MLY-PRCP-75PCTL": [190, 150, 160, 110, 80, 60, 40, 50, 70, 150, 200, 220]
})

austin_weather = pd.DataFrame({
    "MONTH": months,
    "MLY-PRCP-NORMAL": [60, 55, 70, 80, 90, 100, 95, 85, 80, 70, 65, 60],
    "MLY-PRCP-25PCTL": [40, 35, 50, 60, 70, 80, 75, 65, 60, 55, 50, 45],
    "MLY-PRCP-75PCTL": [80, 75, 90, 100, 110, 120, 115, 105, 100, 85, 80, 75]
})

fig, ax = plt.subplots(2, 1 , sharey=True)

ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], linestyle='--', color='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], linestyle='--', color='b')
ax[0].set_ylabel("Precipitation (inches)")

ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], linestyle='--', color='r')
ax[1].plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], linestyle='--', color='r')
ax[1].set_ylabel("Precipitation (inches)")
ax[1].set_xlabel("Time (months)")

plt.show()

# -------------------------------------
# Plotting time-series data?

# Time-series data 
# يعني بيانات بتتسجل بمرور الزمن 
# (زي درجات الحرارة اليومية، أسعار الأسهم كل ساعة، مستوى  شهريًا).

# الهدف من الرسم

# هو إننا نعرض البيانات دي على محور الزمن (x-axis)
# ، ونشوف التغيرات مع الوقت على المحور الرأسي (y-axis).


#-------------------------------

import pandas as pd 
import matplotlib.pyplot as plt 

climate_change = pd.read_csv(r"Introduction to data visualization with Matplotlib\climate_change.csv",
                             parse_dates=["date"] , index_col= "date")


fig,ax = plt.subplots()

ax.plot(climate_change.index , climate_change["co2"])
ax.set_xlabel("Time")
ax.set_ylabel("CO2 (ppm)")
plt.show()

sixties = climate_change["1960-01-01":"1969-12-31"]

fig,ax = plt.subplots()

ax.plot(sixties.index , sixties["co2"])
ax.set_xlabel("Time")
ax.set_ylabel("CO2 (ppm)")
plt.show()


# ------------------------------------
# Plotting time-series with different variables


import pandas as pd 
import matplotlib.pyplot as plt 

climate_change = pd.read_csv(r"Introduction to data visualization with Matplotlib\climate_change.csv",
                             parse_dates=["date"] , index_col= "date")


fig,ax = plt.subplots()

ax.plot(climate_change.index , climate_change["co2"] , color = "b")
ax.set_xlabel("Time")
ax.set_ylabel("CO2 (ppm)" , color = "b")
ax.tick_params("y" ,colors = "b")

ax2 = ax.twinx() # have the same x 

ax2.plot(climate_change.index , climate_change["relative_temp"] , color = "r")
ax2.set_ylabel("relavent Temperature " , color = "r")
ax2.tick_params("y" ,colors = "r")
plt.show()

# -----------------------

# Annotating time-series data

import pandas as pd 
import matplotlib.pyplot as plt 

climate_change = pd.read_csv(r"Introduction to data visualization with Matplotlib\climate_change.csv",
                             parse_dates=["date"] , index_col= "date")


fig,ax = plt.subplots()

ax.plot(climate_change.index , climate_change["co2"] , color = "b")
ax.set_xlabel("Time")
ax.set_ylabel("CO2 (ppm)" , color = "b")
ax.tick_params("y" ,colors = "b")

ax2 = ax.twinx() # have the same x 

ax2.plot(climate_change.index , climate_change["relative_temp"] , color = "r")
ax2.set_ylabel("relavent Temperature " , color = "r")
ax2.tick_params("y" ,colors = "r")

ax2.annotate(">1 degree",
             xy=(pd.Timestamp('1970-03-01'), 0.35),   # نقطة السهم (اخر داتا عندك)
             xytext=(pd.Timestamp('1965-01-01'), 0.10), # مكان النص
             arrowprops={"arrowstyle": "->", "color": "gray"})


plt.show()

# المعنى:

# ax2.annotate
# دي دالة بتستخدم في matplotlib
#  علشان تكتب ملاحظة (annotation) على الرسم البياني،
#  وغالبًا بيكون معاها سهم يوضح نقطة معينة في الرسم.

# ">1 degree"
# النص اللي هيظهر على الرسم (label أو comment).

# xy=(pd.Timestamp('2015-10-06'), 1)
# دي النقطة اللي السهم بيشاور عليها.
# يعني: التاريخ 2015-10-06 على محور الـ x
# ، والقيمة 1 على محور الـ y.
# → السهم هيوصل هنا.

# xytext=(pd.Timestamp('2008-10-06'), -0.2)
# دي النقطة اللي هيظهر عندها النص نفسه.
# يعني هيتكتب النص ">1 degree" عند التاريخ 2008-10-06 والقيمة -0.2.
# → مكان الكتابة مختلف عن مكان السهم.

# arrowprops={}
# دي بتتحكم في شكل السهم (لون – نوع خط – سماكة ...).
# هنا فاضية {}، يعني السهم هيكون بالشكل الافتراضي.

# النتيجة 🎯

# النص ">1 degree" هيتكتب عند (2008, -0.2)، وسهم هيتسحب من النص ده لحد النقطة (2015, 1) على الرسم.


# -------------------------------
# Quantitative comparisons: bar-charts

import matplotlib.pyplot as plt
import pandas as pd
medals = pd.read_csv(r"Introduction to data visualization with Matplotlib\olympics_medals.csv",index_col= 0)
fig , ax = plt.subplots()
ax.bar(medals.index , medals["Gold"])
ax.set_xticklabels(medals.index ,rotation = 45)
ax.set_ylabel("Number of medals")
plt.show()

# -----------------------


import matplotlib.pyplot as plt
import pandas as pd
medals = pd.read_csv(r"Introduction to data visualization with Matplotlib\olympics_medals.csv",index_col= 0)
fig , ax = plt.subplots()
ax.bar(medals.index , medals["Gold"] , label = "Gold")
ax.bar(medals.index , medals["Silver"] , bottom= medals["Gold"] ,label = "Silver")
ax.bar(medals.index , medals["Bronze"] , bottom= medals["Gold"] + medals["Silver"] , label = "Bronze")
ax.set_xticklabels(medals.index ,rotation = 45)
ax.set_ylabel("Number of medals")
ax.legend()
plt.show()


# Quantitative comparisons: histograms
# الداتا مش موجوده بس الفكره واضحه :)
fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"] , label = "Rowing" , histtype = "step")

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"], label = "Gymnastics",histtype = "step")

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()


# histtype = "step" -> هتخليه مش مجوف , هيبقي شفاف علشان نقدر نشوف اللي ورا

# ------------------------------------------

# Adding error bars to bar charts

import matplotlib.pyplot as plt
import pandas as pd

mens_rowing = pd.DataFrame({"Height": [190, 195, 200, 185, 188]})
mens_gymnastics = pd.DataFrame({"Height": [160, 165, 162, 158, 164]})

fig, ax = plt.subplots()

ax.bar("Rowing",
       mens_rowing["Height"].mean(),
       yerr=mens_rowing["Height"].std())

ax.bar("Gymnastics",
       mens_gymnastics["Height"].mean(),
       yerr=mens_gymnastics["Height"].std())

ax.set_ylabel("Height (cm)")
plt.show()


# إيه هي الشرطة (Error Bar)؟ -> yerr

# الـ Error Bar هو خط صغير فوق وتحت العمود أو النقطة في الرسم.

# بيمثل مدى عدم اليقين أو التشتت حوالين القيمة.

# في المثال بتاعك، إحنا استخدمنا الانحراف المعياري (std)، اللي بيقيس مدى تفرق البيانات عن المتوسط.

# 🔹 ليه مهم؟

# خليني أديك مثال مبسط:

# عندي رياضتين:

# Rowing: أطوال اللاعبين [190, 195, 200, 185, 188]

# Gymnastics: أطوال اللاعبين [160, 165, 162, 158, 164]

# الاتنين ليهم متوسط:

# Rowing ≈ 192.6 سم

# Gymnastics ≈ 161.8 سم

# لكن:

# الانحراف المعياري (Rowing) ≈ 5.6 → يعني فيه اختلاف بسيط بين اللاعبين.

# الانحراف المعياري (Gymnastics) ≈ 2.6 → يعني اللاعبين أقرب لبعض في الطول.

# 🔹 الشرطة بتقول إيه في الرسم؟

# لو الشرطة قصيرة → البيانات كلها قريبة من بعضها (اللاعبين شبه بعض).

# لو الشرطة طويلة → فيه تفاوت كبير بين اللاعبين.

# مثال:

# في Rowing → الشرطة أطول شوية → اللاعبين أطوالهم مختلفة بشكل أوضح.

# في Gymnastics → الشرطة أقصر → كلهم شبه بعض في الطول.


# --------------------------------

fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"], yerr= seattle_weather["MLY-TABG-STDDEV"])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"], yerr= austin_weather["MLY-TABG-STDDEV"])
 

# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()

# الكود بيعمل إيه؟

# errorbar → بيعمل خط (line plot) ومعاه error bars (خطوط صغيرة فوق وتحت كل نقطة).

# بيتكرر مرتين: مرة لـ Seattle ومرة لـ Austin.

# المعطيات:

# MONTH → محور X (الشهور).

# MLY-TAVG-NORMAL → المحور Y (متوسط درجة الحرارة الشهرية).

# yerr=MLY-TABG-STDDEV → بيضيف Error Bars (الانحراف المعياري في درجات الحرارة).

# 🔹 النتيجة البصرية

# هتشوف خطين:

# واحد لدرجات الحرارة في Seattle.

# واحد لدرجات الحرارة في Austin.

# كل نقطة في الخط هي متوسط درجة الحرارة في الشهر ده.

# الشرطة (Error Bar) حوالين النقطة بتوضح مدى التغير (التقلب) في درجات الحرارة.

# 🔹 القيمة “المهنية” (ليه أستخدمه؟)

# ده مفيد جدًا في تحليل بيانات الطقس أو أي بيانات طبيعية:

# مش بس يوريك المتوسط (الخط).

# لكن كمان يوريك مدى التغير أو التذبذب حوالين المتوسط.

# مثلاً:

# لو في شهر Seattle الشرطة صغيرة → يعني درجات الحرارة في الشهر ده شبه ثابتة (مفيش تفاوت كبير).

# لو في شهر Austin الشرطة كبيرة → يعني الشهر ده فيه تفاوت أو تقلب كبير في الحرارة (مثلاً يوم حر جدًا ويوم بارد).


# Adding Box Plot 


import matplotlib.pyplot as plt
import pandas as pd

mens_rowing = pd.DataFrame({"Height": [190, 195, 200, 185, 188]})
mens_gymnastics = pd.DataFrame({"Height": [160, 165, 162, 158, 164]})

fig, ax = plt.subplots()

ax.boxplot([mens_rowing["Height"], mens_gymnastics["Height"]])
ax.set_xticklabels(["Rowing", "Gymnastics"])
ax.set_ylabel("Height (cm)")
plt.show()


# -----------------------------------------------

# Quantitative comparisons: scatter plots

import pandas as pd 
import matplotlib.pyplot as plt 

climate_change = pd.read_csv(r"Introduction to data visualization with Matplotlib\climate_change.csv"
                            )


fig,ax = plt.subplots()

ax.scatter(climate_change["co2"] ,climate_change["relative_temp"],c = climate_change.index )
ax.set_xlabel("Time")
ax.set_ylabel("CO2 (ppm)" , color = "b")
plt.show()


# ========================================

# Preparing your figures to share with others


import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

seattle_weather = pd.DataFrame({
    "MONTH": months,
    "MLY-PRCP-NORMAL": [145, 110, 120, 80, 60, 40, 20, 25, 50, 110, 160, 180],
    "MLY-PRCP-25PCTL": [100, 80, 90, 60, 40, 20, 10, 15, 30, 80, 120, 130],
    "MLY-PRCP-75PCTL": [190, 150, 160, 110, 80, 60, 40, 50, 70, 150, 200, 220]
})

austin_weather = pd.DataFrame({
    "MONTH": months,
    "MLY-PRCP-NORMAL": [60, 55, 70, 80, 90, 100, 95, 85, 80, 70, 65, 60],
    "MLY-PRCP-25PCTL": [40, 35, 50, 60, 70, 80, 75, 65, 60, 55, 50, 45],
    "MLY-PRCP-75PCTL": [80, 75, 90, 100, 110, 120, 115, 105, 100, 85, 80, 75]
})

plt.style.use("ggplot") # شكل الرسم 

fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])
ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
plt.show()

# OR


import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

seattle_weather = pd.DataFrame({
    "MONTH": months,
    "MLY-PRCP-NORMAL": [145, 110, 120, 80, 60, 40, 20, 25, 50, 110, 160, 180],
    "MLY-PRCP-25PCTL": [100, 80, 90, 60, 40, 20, 10, 15, 30, 80, 120, 130],
    "MLY-PRCP-75PCTL": [190, 150, 160, 110, 80, 60, 40, 50, 70, 150, 200, 220]
})

austin_weather = pd.DataFrame({
    "MONTH": months,
    "MLY-PRCP-NORMAL": [60, 55, 70, 80, 90, 100, 95, 85, 80, 70, 65, 60],
    "MLY-PRCP-25PCTL": [40, 35, 50, 60, 70, 80, 75, 65, 60, 55, 50, 45],
    "MLY-PRCP-75PCTL": [80, 75, 90, 100, 110, 120, 115, 105, 100, 85, 80, 75]
})

plt.style.use("tableau-colorblind10") # شكل الرسم 

fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])
ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
plt.show()


#OR


import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

seattle_weather = pd.DataFrame({
    "MONTH": months,
    "MLY-PRCP-NORMAL": [145, 110, 120, 80, 60, 40, 20, 25, 50, 110, 160, 180],
    "MLY-PRCP-25PCTL": [100, 80, 90, 60, 40, 20, 10, 15, 30, 80, 120, 130],
    "MLY-PRCP-75PCTL": [190, 150, 160, 110, 80, 60, 40, 50, 70, 150, 200, 220]
})

austin_weather = pd.DataFrame({
    "MONTH": months,
    "MLY-PRCP-NORMAL": [60, 55, 70, 80, 90, 100, 95, 85, 80, 70, 65, 60],
    "MLY-PRCP-25PCTL": [40, 35, 50, 60, 70, 80, 75, 65, 60, 55, 50, 45],
    "MLY-PRCP-75PCTL": [80, 75, 90, 100, 110, 120, 115, 105, 100, 85, 80, 75]
})

plt.style.use("grayscale") # شكل الرسم 

fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])
ax.set_xlabel("Time (months)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")
plt.show()

# -----------------------------------------

# Sharing your visualizations withothers

import matplotlib.pyplot as plt
import pandas as pd
medals = pd.read_csv(r"Introduction to data visualization with Matplotlib\olympics_medals.csv",index_col= 0)
fig , ax = plt.subplots()
ax.bar(medals.index , medals["Gold"])
ax.set_xticklabels(medals.index ,rotation = 45)
ax.set_ylabel("Number of medals")
fig.set_size_inches([5,8]) # width , heigth

fig.savefig("gold_medals.jpg") # to save jpg 
fig.savefig("gold_medals.png") # to save png 


# Thank you :) 