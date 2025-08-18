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

# Sampling with/without replacement in Python\
print(data.sample(5, replace = True))

# --------------------------
# Continuous distributions

# عندنا مثلا بيانات من 0 الي 12 و عايزين نسبه ان يطلع اقل من 7 
from scipy.stats import uniform
x = uniform.cdf(7, 0, 12)
print(x)

# P(wait time≥7)=1−P(wait time≤7)

from scipy.stats import uniform
x = 1 - uniform.cdf(7,0, 12)
print(x)

# P(4 ≤ wait time ≤ 7)

from scipy.stats import uniform

x = uniform.cdf(7,0,12)- uniform.cdf(4,0,12)
print(x)

#P(0≤outcome≤12)

from scipy.stats import uniform

x = uniform.cdf(12,0,12) # 1
print(x)

# Generating random numbers according to uniformdistribution

from scipy.stats import uniform 

x = uniform.rvs(0 , 15 , size = 100) # form 0 to 15 generate 100 element
print(x)
# The binomial distribution

# Coin flipping 
# Head == success == 1
# Tail == Failure == 0

# A single flip
# binom.rvs(# of coins, probability of heads/success, size=# of trials)

from scipy.stats import binom

x = binom.rvs(1 , 0.5 ,size = 10) # will return array , contain number of head in each trials 
print(x)

from scipy.stats import binom
x = binom.rvs(10, 0.5 , size =10 )
print(x)


from scipy.stats import binom
x = binom.rvs(10, 0.1 , size =10 )
print(x)


# P(heads=7)
# binom.pmf(num heads, num trials, prob of heads)

from scipy.stats import binom
x = binom.pmf(7,10,0.5)
print(x)


# P(heads≤7)
# binom.cdf(num heads, num trials, prob of heads)

from scipy.stats import binom
x = binom.cdf(7, 10, 0.5)
print(x)

# P(heads>7)

from scipy.stats import binom
x = 1- binom.cdf(7, 10, 0.5)
print(x)

# Expected value = n × p
# Expected number of heads out of 10 flips = 10 × 0.5 =5

# More Distributions and the Central Limit Theorem

# norm.cdf(الرقم اللي عايز تعرف الاحتمال لغاية عنده , mean , standard deviation)
# P(x <= 154 )

from scipy.stats import norm
x = norm.cdf(154 , 161 , 7 )
print(x)
# P(x >= 154 )

from scipy.stats import norm
x = 1 - norm.cdf(154,161,7)
print(x)

# P(x > 154 and x < 157)

from scipy.stats import norm
x = norm.cdf(157,161,7) - norm.cdf(154,161,7)
print(x)

# What height are 90% -> from left 
# norm.ppf(precentage , mean , std)
# norm.ppf هو العكس بتاع cdf

# يعني بدل ما تقول: "الاحتمال لحد قيمة معينة كام؟"

# بتقول: إيه هي القيمة اللي تخلي الاحتمال
#  يوصل لنسبة معينة (من الشمال)؟"

from scipy.stats import norm
x = norm.ppf(0.9 , 161 , 7)
print(x)

# From right

from scipy.stats import norm
x = norm.ppf(1 - 0.9 , 161 , 7)
print(x)


# Generating random number 

# norm.rvs(mean , std , size )

from scipy.stats import norm 
x = norm.rvs(161 , 7 , size = 10)
print(x)

# Central limit theorem

# The sampling distribution of a statistic
#  becomes closer to the normal distribution as 
#  the number of trials increases.


# The Poisson distribution

# probability of some # of events occurring over a fixed
# period of time 

# Lambda - > average number of events per time interval 

# if the average number of adoptions per week is 8,
# what is P( # adoptions in a week = 5)

from scipy.stats import poisson

# poisson(number , lambda)
x = poisson.pmf(5,8)
print(x)


# p(# adoptions in a week <= 5)

from scipy.stats import poisson
x = poisson.cdf(5 , 8)
print(x)

# p(# adoptions in a week > 5)

from scipy.stats import poisson
x = 1 - poisson.cdf(5 , 8)
print(x)

# sampling from a poisson distribution
from scipy.stats import poisson
x = poisson.rvs(8 , size = 10)
print(x) 
