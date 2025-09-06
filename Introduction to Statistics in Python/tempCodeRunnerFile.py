# probability 

# p(event) = (# ways event can happen) / (total # of possible outcomes)

# Sampling from a DataFrame

import numpy as np
import pandas as pd
dic = {
    "name" : ["ahmed" , "nada" ,"abdo" , "hussein", "alaa"  ],
    "age" :  [20,28,18,59,26]
}

data  = pd.DataFrame(dic)
print(data.sample())
print("\n\n")
print(data.sample(2))
print("\n\n")

# Setting a random seed

np.random.seed(10) # هتثبت الناتج 
print(data.sample())
print("\n\n")
print(data.sample())
print("\n\n")