# import numpy for analysis
import numpy as np

# import scipy to dinf mode
from scipy import stats as st

# IMPORT matplotlib for visualization
import matplotlib.pyplot as mpp

# generate data randomly 
data = np.random.uniform(0.0,5.0,100000)

# find the mean 
mean = np.mean(data)

# find the median
median = np.median(data)

# find the mode 
mode = st.mode(data)

# find the standard deviation
std = np.std(data)

# find the variation
v = std * 2

# find the coeeficient of variation
cv = (std / mean) * 100


print(" mean :" + str(mean))
print("")
print(" median :" + str(median))
print("")
print(" mode :" + str(mode))
print("")
print(" standard deviation :" + str(std))
print("")
print(" varience :" + str(v))
print("")
print(" coefficient of variation :" + str(cv))
print("")

mpp.hist(data , 5)
mpp.show()