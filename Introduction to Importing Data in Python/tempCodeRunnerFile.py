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