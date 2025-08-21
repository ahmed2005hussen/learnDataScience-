# What is seaborn ? 
# python data visualization library 
# Easily create the most common types of plots 

import seaborn as sns  
import matplotlib.pyplot as plt 

height = [62,64,69,75,66,68,65,71,76,73]
weight = [120 , 136,148,175,137,165,154,172,200,187]

sns.scatterplot(x = height , y = weight)
plt.show()


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import seaborn as sns
import matplotlib.pyplot as plt 

gender = ["Female" ,"Female" , "Female" ,"Female" ,
          "Male","Male","Male","Male","Male","Male"]

sns.countplot(x=gender, palette={"Female": "red", "Male": "blue"})
plt.show()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Using pandas with Seaborn

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("Country.csv")
sns.countplot(x = "country"  , data = df )
plt.show()

# =================================

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.scatterplot(x = "total_bill" , y = "tip" , data = tips,
                hue="smoker"  )
# hue="smoker" →
# يعطي لكل فئة (مدخن أو غير مدخن) لون مختلف لتسهيل التمييز بينهما.
plt.show()
print(tips.head())

# =================================
# Change order 
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.scatterplot(x = "total_bill" , y = "tip" , data = tips,
                hue="smoker" , hue_order=["No" ,"Yes"]  )
plt.show()
print(tips.head())

# =================================
# Change color 

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

hue_colors = {"Yes" : "black" , "No" : "red"}
sns.scatterplot(x = "total_bill" , y = "tip" , data = tips,
                hue="smoker" , palette= hue_colors)
plt.show()
print(tips.head())

# ============================================

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.countplot(x = "smoker" , data= tips , hue="sex")
plt.show()

# -----------------------------------

# relplot
# relplot -> relationship plot (Scatter , line plots)
# أي رسم العلاقة بين متغيرين 

# يضيف ميزة إضافية: سهولة إنشاء Facets / Subplots باستخدام col و row بدون الحاجة لاستخدام plt.subplot يدوياً.

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.relplot(x = "total_bill" , y = "tip" , data = tips , kind="scatter")
plt.show()

# =========================

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.relplot(x = "total_bill" , y = "tip" , data = tips , kind="scatter" , col="smoker")
plt.show()
# =========================

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.relplot(x = "total_bill" , y = "tip" , data = tips , kind="scatter" , row="smoker")
plt.show()
# =========================

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.relplot(x = "total_bill" , y = "tip" , data = tips ,
             kind="scatter" , col="smoker" , row = "time")
plt.show()
# =========================

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.relplot(x = "total_bill" , y = "tip" , data = tips ,
             kind="scatter" , col="day" , col_wrap=3) # col wrap -> number of column
plt.show()
# ==============================
# Customizing scatter plots
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.relplot(x = "total_bill" , y = "tip" , data = tips ,
             kind="scatter" , size="size") 
plt.show()
# رغم اننا عملنا الدواير علي اساس العدد بس لسه مش واضح اوي 

# ----------------------------
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.relplot(x = "total_bill" , y = "tip" , data = tips ,
             kind="scatter" , size="size" , hue = "size") 
plt.show()
# كده بقا اوضح 

#=================================

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.relplot(x = "total_bill" , y = "tip" , data = tips ,
             kind="scatter" , style="smoker" , hue = "smoker") 
plt.show()

# -----------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

sns.relplot(x = "total_bill" , y = "tip" , data = tips ,
             kind="scatter" , style="smoker" , hue = "smoker" , alpha = 0.3) 
plt.show()
# =======================================

# introduction to line plots 

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.relplot(x="hour", y="NO_2",data=air_df,kind="line")
# plt.show()

# ممكن يظهر shadow 
# حوالين الخط 

# Shaded region is the confidence interval
# Assumes dataset is a random sample 
# 95% confident that the mean is within this interval 
# Indicates uncertainty in our estimate

# ==================================

# Replacing confidence interval with standard deviation

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.relplot(x="hour", y="NO_2",data=air_df,kind="line",ci="sd")
# plt.show()

#================================

# Turning off confidence interval

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.relplot(x="hour", y="NO_2",data=air_df,kind="line",ci=None)
# plt.show()
#--------------------------

# Import Matplotlib and Seaborn
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Add markers and make each line have the same style
# sns.relplot(x="model_year", y="horsepower", 
#             data=mpg, kind="line", 
#             ci=None, style="origin", 
#             hue="origin",
#             markers = True, 
#             dashes = False)

# # Show plot
# plt.show()

# ---------------------

# catplot() -> categorical plots 
# (countplot , barplot , boxplot, pointplot)

# g = sns.catplot(x="time",y="total_bill",data=tips,kind="box",sym="") 
# # sym -> remove outlier
# plt.show()

# ------------
# 1️⃣ countplot

# ماذا يفعل؟

# يعدّ عدد مرات ظهور كل فئة في عمود تصنيفي (categorical column).

# مثال: عدد الذكور والإناث في بيانات العملاء.

# متى تستخدم؟

# لما تريد رؤية توزيع الفئات وعددها.

# أهميته:

# يعطيك فكرة واضحة عن توازن البيانات أو الفئات الغالبة.

# sns.countplot(x="sex", data=tips)

# 2️⃣ barplot

# ماذا يفعل؟

# يرسم متوسط قيمة متغير كمي لكل فئة تصنيفية.

# مثال: متوسط البقشيش (tip) لكل يوم (day).

# متى تستخدم؟

# لما تريد مقارنة متوسطات القيم بين الفئات.

# أهميته:

# يساعدك على رؤية الاختلافات بين المجموعات بسهولة.

# sns.barplot(x="day", y="tip", data=tips)


# ملاحظة: عادة يظهر مع فترة ثقة (CI) حول المتوسط.

# 3️⃣ boxplot

# ماذا يفعل؟

# يوضح توزيع البيانات داخل كل فئة: الحد الأدنى، الحد الأقصى، الوسيط، والـ quartiles، وأحيانًا القيم الشاذة (outliers).

# مثال: توزيع البقشيش لكل يوم.

# متى تستخدم؟

# عندما تريد فهم شكل توزيع البيانات واكتشاف القيم الشاذة.

# أهميته:

# يعطيك رؤية دقيقة للتشتت والانتشار، وليس فقط المتوسط.

# sns.boxplot(x="day", y="tip", data=tips)

# 4️⃣ pointplot

# ماذا يفعل؟

# يشبه barplot لكنه يستخدم نقاط وخطوط لربط المتوسطات بين الفئات.

# مثال: تتبع متوسط البقشيش لكل يوم عبر أوقات مختلفة (time).

# متى تستخدم؟

# عندما تريد مقارنة الاتجاهات بين الفئات وليس فقط القيم الفردية.

# أهميته:

# ممتاز لرؤية الاتجاهات والتغيرات بين الفئات عبر متغير آخر.

# sns.pointplot(x="day", y="tip", hue="time", data=tips)

# الخلاصة العملية:
# الرسم	يركز على	مثال عملي	مفيد لـ…
# countplot	عدد الفئات	عدد الذكور والإناث	معرفة توزيع الفئات
# barplot	متوسط القيم	متوسط البقشيش لكل يوم	مقارنة الفئات
# boxplot	توزيع البيانات	توزيع البقشيش لكل يوم	رؤية التشتت والقيم الشاذة
# pointplot	الاتجاهات	متوسط البقشيش لكل يوم عبر الوقت	رؤية التغيرات والاتجاهات

# 💡 نصيحة:

# إذا تريد فهم الفئات وعددها → countplot.

# إذا تريد مقارنة متوسطات → barplot أو pointplot.

# إذا تريد رؤية التوزيع بالكامل → boxplot.

# ------------------------------
# Changing plot style and color


import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

sns.set_style("dark") # defaulte -> white 
sns.set_palette("GnBu")
sns.set_context("talk") # defaulte -> paper 
tips = sns.load_dataset("tips")

sns.countplot(x = "smoker" , data= tips , hue="sex")
plt.show()

# -------------------------------------
# Adding titles and labels

import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

tips = sns.load_dataset("tips")

g = sns.relplot(x = "total_bill" , y = "tip" , data = tips , 
             kind="scatter" , size="size" , hue = "size") 

# g -> object FactGrid
g.fig.suptitle("This title" , y = 1) # -> y defaulte = 1 , هنرفعه شويه لفوق
g.set(xlabel= "x-axis" , ylabel="y-axis")
plt.show()

# -------------------------------------

import seaborn as sns  
import matplotlib.pyplot as plt 

height = [62,64,69,75,66,68,65,71,76,73]
weight = [120 , 136,148,175,137,165,154,172,200,187]

g = sns.scatterplot(x = height , y = weight)
# g -> object AxesSubPlot

g.set_title("this is title")
plt.xticks(rotation=90)

plt.show()

