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

x = "ahmed"
print(x.upper())
print(x.lower())
print(x.capitalize())


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

