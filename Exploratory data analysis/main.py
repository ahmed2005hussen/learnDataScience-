# Exploratory Data Analysis
# The process of reviewing and cleaning data to
# 1- derive insights
# 2- generate hypotheses

import pandas as pd

df = pd.read_csv("Country.csv")
print(df.dtypes)

# if you want to change data type for column 

df["area"] = df["area"].astype("int")
print(df.dtypes)

# if you want to show a specific data type columns: 

print(df.select_dtypes("object") , "\n\n")
print(df.select_dtypes("number"), "\n\n")

print(df["area"].min())
print(df["area"].max())
print("\n\n")
# -------------
x = df.agg({"area": ["mean", "std"], "population": ["median"]})
print(x)

x = df.groupby("country").agg(

    mean_area = ("area"  , "mean"),
    std_area = ("area" , "std"),

)

print(x)


# Addressing missing value 

# 1- Drop missing values 5% or less of total values
# 2- Impute mean, median, mode Depends on distribution and context
# 3- Impute by sub-group:
# Different experience levels have different median salary

# يعني إيه Impute by sub-group؟

# بدل ما تملا القيم الناقصة  بقيمة واحدة على مستوى الداتا كلها (زي المتوسط )،
#  بنقسم الداتا لمجموعات منطقية مثلاً حسب خبرة الموظف 
# (Junior/Mid/Senior)
# وبعدين نملأ القيم الناقصة بإحصائية من نفس المجموعة (غالبًا الوسيط لأنه مقاوم للقيم الشاذة).
# الفكرة: رواتب الـ Senior أعلى من Junior، فلو مليت NaN بوسيط كل مجموعة هتحافظ على الفروقات الطبيعية بين المجموعات.

import pandas as pd
df = pd.read_csv("employee_salaries_original.csv")

# print number of nan value 

print(df.isna().sum())

# 1- first method drop less 5%

threshold = len(df) * 0.05

cols_drop = df.columns[(df.isna().sum() <= threshold ) & (df.isna().sum() != 0)]

df.dropna(subset=cols_drop , inplace= True)
print(df.isna().sum())

# Method 2 

cols_with_missing_values = df.columns[df.isna().sum() > 0 ]

for col in cols_with_missing_values: 
    df[col].fillna(df[col].mode()[0] , inplace= True)

print(df.isna().sum())

# method 3 

import pandas as pd
df = pd.read_csv("employee_salaries_original.csv")

salaries_dict = df.groupby("experience_level")["salary"].median().to_dict()
print(salaries_dict)

df["salary"] = df["salary"].fillna(df["experience_level"].map(salaries_dict))
print(df.isna().sum())

# -----------------------

# Converting and analyzing categorical data

import pandas as pd
df = pd.read_csv("employee_salaries_original.csv")

print(df["experience_level"].nunique(),"\n\n")

check = df["experience_level"].str.contains("ior")
print(df[check],"\n\n")

# Senior or junior
check = df["experience_level"].str.contains("Senior|Junior") 
print(df[check],"\n\n")

# start with :

check = df["experience_level"].str.contains("^S")
print(df[check],"\n\n")

# --------------

# 1. عندك مسميات وظيفية كتيرة ومختلفة

# مثلاً في عمود Designation ممكن تلاقي:

# "Senior Data Scientist"

# "NLP Engineer"

# "Data Analyst Intern"

# "ETL Architect"

# "AI Researcher"

# "Lead Data Engineer"

# "Freelance Consultant"
# وهكذا…

# لو فضلت تشتغل بالمسميات دي هتلاقي عندك عشرات أو مئات الأسماء المختلفة.

# 2. الهدف → توحيد المسميات تحت فئات كبرى

# فعملت لستة بالفئات الرئيسية:

# job_categories = ["Data Science", "Data Analytics", "Data Engineering", 
#                   "Machine Learning", "Managerial", "Consultant"] 

# 3. تعريف الـ Regex Patterns لكل فئة

# كتبت Strings فيها كلمات مفتاحية (regular expressions):

# data_science = "Data Scientist|NLP"
# data_analyst = "Analyst|Analytics"
# data_engineer = "Data Engineer|ETL|Architect|Infrastructure"
# ml_engineer = "Machine Learning|ML|Big Data|AI"
# manager = "Manager|Head|Director|Lead|Principal|Staff"
# consultant = "Consultant|Freelance"


# المعنى: لو الـ Designation يحتوي أي كلمة من دول → يبقى ينتمي للفئة دي.
# مثلاً: "Senior NLP Engineer" هيمسك كلمة NLP → يتصنف كـ Data Science.

# 4. conditions
# conditions = [
#     (salaries["Designation"].str.contains(data_science)),
#     (salaries["Designation"].str.contains(data_analyst)),
#     (salaries["Designation"].str.contains(data_engineer)),
#     (salaries["Designation"].str.contains(ml_engineer)),
#     (salaries["Designation"].str.contains(manager)),
#     (salaries["Designation"].str.contains(consultant))
# ]


# دي عبارة عن قائمة boolean masks (True/False) على حسب وجود الكلمة المفتاحية في العمود.

# 5. np.select
# salaries["Job_Category"] = np.select(
#     conditions,
#     job_categories,
#     default="Other"
# )


# np.select بياخد الـ conditions ويقارنها بالـ job_categories بالترتيب.

# أول condition تطلع True → يدي العمود القيمة المناظرة من job_categories.

# لو مفيش ولا واحدة تنطبق → يصنفها "Other".

# -----------------------

# Working with numeric data

# pd.Series.str.replace("characters to remove", "characters to replace them with")

#salaries["Salary_In_Rupees"] = salaries["Salary_In_Rupees"].str.replace(",", "")

import pandas as pd 

salaries = {"Salary_In_Rupees": ["12,12,3" , "31,41,2" , "5,31,3"] , 
            "Salary_USD" : [12,123,32] ,
            "Experience": ["a" ,"a" , "b"]}

df = pd.DataFrame(salaries)

print(df)

df["Salary_In_Rupees"] = df["Salary_In_Rupees"].str.replace(",","")
print(df)
 
print(df["Salary_In_Rupees"].dtypes) # Object 

df["Salary_In_Rupees"] = df["Salary_In_Rupees"].astype("float")
print(df["Salary_In_Rupees"].dtypes) # float 

df["std_dev"] = df.groupby("Experience")["Salary_USD"].transform(lambda x : x.std())
print(df)

# df["std_dev"] = df.groupby("Experience")["Salary_USD"].transform(lambda x: x.std())
# هنا transform بترجع Series بنفس طول DataFrame الأصلي.

# لكل صف، بتكتبله الـ std الخاص بالجروب اللي بينتمي له.

# يعني: لو عندك 100 صف، العمود الجديد هيكون برضه 100 صف.


# ------------------------------------

# Handling outliers 
# لو البيانات حقيقيه فا غالبا هنسيبها حتي لو في outlier
# لو البيانات مشكوك في صحتها , هنشيلها 

# Patterns over time

import pandas as pd

# To convert object type into date type
df= pd.read_csv("divorce.csv", parse_dates=["marriage_date"])
print(df["marriage_date"].dtype)

# OR

df= pd.read_csv("divorce.csv")

df["marriage_date"] = pd.to_datetime(df["marriage_date"])
print(df["marriage_date"].dtype)


import pandas as pd

df= pd.read_csv("divorce.csv")

# Creating datatime data 

df["marriage_date"] = pd.to_datetime(df["marriage_date"])

df["month"] = df["marriage_date"].dt.month
df["day"] = df["marriage_date"].dt.day
df["year"] = df["marriage_date"].dt.year
print(df)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Correlation
# Describes direction and strength of relationship between two variables

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df= pd.read_csv("divorce.csv")
cor = df.corr(numeric_only=True)
print(cor)

sns.heatmap(cor , annot=True)  # , annot=True -> set the number in the heatmap 
plt.show()

# relation between this columns in scatter plot
sns.pairplot(data=df, vars=["income_man", "income_woman", "marriage_duration"])
plt.show()


#1. Scatter Plots بين كل عمودين

# يرسم لك scatter plot لكل زوج من الأعمدة اللي اخترتهم.
# مثلاً:

# محور X = income_man، محور Y = income_woman

# محور X = income_man، محور Y = marriage_duration

# محور X = income_woman، محور Y = marriage_duration

# وبكده تقدر تشوف العلاقة بين كل اتنين.

# 2. توزيعات الأعمدة نفسها (diagonal)

# على القطر (diagonal) بيعرض histogram أو KDE (distribution) لكل عمود لوحده، عشان تعرف شكل توزيع البيانات.

# 3. الهدف الأساسي

# يساعدك تكتشف بسرعة العلاقات والارتباطات بين المتغيرات.

# تشوف إذا فيه علاقة خطية (linear)، أو غير خطية، أو مفيش علاقة.

# تشوف الـ outliers (قيم شاذة).



# ------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df= pd.read_csv("divorce.csv")
sns.kdeplot(data=df, x="marriage_duration", hue="education_man")
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df= pd.read_csv("divorce.csv")
sns.kdeplot(data=df, x="marriage_duration", hue="education_man" , cut = 0)
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df= pd.read_csv("divorce.csv")
sns.kdeplot(data=df, x="marriage_duration", hue="education_man" , cut = 0 , cumulative=True)
plt.show()

# --------------------

# Why perform EDA?
# Detecting patterns and relationships
# Generating questions, or hypotheses
# Preparing data for machine learning




# pd.crosstab(
#     planes["Source"], 
#     planes["Destination"], 
#     values=planes["Price"], 
#     aggfunc="median"
# )
# 1. pd.crosstab
# بتعمل جدول ملخص (pivot-style table).

# الصفوف = القيم في العمود الأول (Source)

# الأعمدة = القيم في العمود الثاني (Destination)

# 2. values=planes["Price"]
# بدل ما تحسب عدّ (count) زي ما الـ crosstab بيعمل عادة، هنا بتاخد عمود "Price" وتطبّق عليه دالة تجميع (aggregation).

# 3. aggfunc="median"
# بدل الـ sum أو mean، هنا بتاخد الوسيط (median) لسعر الرحلة (Price) بين كل زوج (Source, Destination).

# 4. النتيجة:
# جدول ثنائي الأبعاد:

# الـ صفوف = مدن المغادرة (Source).

# الـ أعمدة = مدن الوصول (Destination).

# الـ قيم الجدول = الـ median لأسعار التذاكر من المصدر إلى الوجهة.

# 📊 مثال (افتراضي):

# Source	Delhi	Mumbai	Chennai
# Kolkata	4500	5200	6100
# Delhi 	NaN	    4000	4800
# Mumbai	4200	NaN	    5000

# ده معناه مثلاً إن:

# median سعر الرحلة من Kolkata → Mumbai هو 5200.

# من Delhi → Chennai هو 4800.

# لو مفيش رحلة بين مدينتين → تطلع NaN.


# --------------------------

import pandas as pd

planes = pd.DataFrame({
    "Price": [100, 200, 300, 400, 500, 600, 1000, 2000]
})


twenty_fifth = planes["Price"].quantile(0.25)
median = planes["Price"].median()
seventy_fifth = planes["Price"].quantile(0.75)
maximum = planes["Price"].max()

labels = ["Economy", "Premium Economy", "Business Class", "First Class"]
bins = [0, twenty_fifth, median, seventy_fifth, maximum]

planes["Price_Category"] = pd.cut(planes["Price"],labels=labels, bins=bins)
print(planes)

#النتيجة: الكود بيقسم الأسعار لمستويات (Economy → First Class) حسب توزيعها (quartiles + max).

# -------------------------

# Generating hypotheses
