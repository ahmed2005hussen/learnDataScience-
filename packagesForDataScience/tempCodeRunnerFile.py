groupBy = data.pivot_table(values="temperature_c",index="store" , columns="department", aggfunc=["median" , "mean"] , fill_value=0 , margins=True)
print(groupBy)