
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
