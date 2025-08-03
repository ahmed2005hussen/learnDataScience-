# here we will discuess the rules and guidelines for named variable 
"""
1- don't start with number 
2- don't use any special character like {@ $ ! , ....}
3- can start with underscore _
4- can include _ or number in or last your variable 
5- use snake_case for named your long variable 
5- shouldn't use l or o to named variable as it could be confusing with 1 or 0
"""






# concatenat 
firstName = "ahmed "
lastName = "hussein"
fullName = firstName + lastName 
print(fullName)

age = 50 
print(fullName + str(age))

# IN and Not IN

txt = "Ahmed hussein"

print("Ahmed" in txt )     # true
print("Ahmed" not in txt ) # false 
print("\n")

# ------------------------------------

# Slicing 

# possitive index 
x = "ahmed Hussein"
print(x[0:5])
print(x[:5])


print(x[::2]) # two step 

# negative index 
print(x[-13:-8])
print("\n")

# ------------------------------------
# Split 
x = "ahmed H u s sein"
print(x.split(' '))
print(x.split(' ',2)) # split(separator , maxsplit )
print("\n")

# ------------------------------------
# Format 
x = "ahmed"
y = "hussein"
print(f"my name is {x} and my father name is {y}") 
print("\n")

# ------------------------------------
# replace 
x = "ahmed"
print(x.replace('h','A'))
print(x.replace('hme','A'))
print("\n")

# ------------------------------------
# escape characters 

print("ahmed \nhussein") # new line 
print("The date now is 30\\07\\2025") # backSlach 
print("'ahmed'") # without any escape characters 
print('\'ahmed\' ') # to make '' in '' for strings 
print("\"ahmed\"")# to make "" in "" for strings 
print("ahmed\rAHM") # replace Strings after \r in begin the string before \r -> AHMed
print("This is \t tab ")
print("\n")

# ------------------------------------
# String Methods

x = "ahmed hussein"
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.title())

x = "HussEin"
print(x.casefold()) # first letter will be small 
print("\n")

x = "ahmed hussein"
print(x.center(15)) # it see the length of the string and if the prameter is larger it will be move string to center it 

print(x.count("s")) # Count something in string 
print(x.endswith("n"))
print(x.endswith("C"))
print("\n")



x = "Hello\tWorld"
print(x.expandtabs(11))
print(x.find("H"))

x = "ahmed{c}"
print(x.format(c = 12))

print("\n")
x = "ahmed"
y = "ahmed121"
z = "ahmed 8"
print(x.isalnum() , " " , y.isalnum(), " " , z.isalnum()) # check if all char in string are alphabet and numbers only
print("\n")

x = "ahmed"
y = "ahmed121"
z = "ahmed a"
print(x.isalpha() , " " , y.isalpha(), " " , z.isalpha()) # check if all char in string are alphabet only
print("\n")


print("123".isdecimal())   # ✅ True -> 0 to 9 only 
print("123".isdigit())     # ✅ True -> any number 

print("²".isdecimal())     # ❌ False
print("²".isdigit())       # ✅ True

print("١٢٣".isdecimal())   # ✅ True 
print("١٢٣".isdigit())     # ✅ True

print("½".isdecimal())     # ❌ False
print("½".isdigit())       # ❌ False

print("\n")

print("123".isnumeric()) # ✅ True 
print("12 3".isnumeric())# ❌ False

# --------------------------

