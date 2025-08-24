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

