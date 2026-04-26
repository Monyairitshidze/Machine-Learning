# import numpy 
import numpy as np

# import stats
from scipy import stats as st

# import matplotlib for visualizasion
import matplotlib.pyplot as mp

# create data randomly so
hours_studied = list(np.random.uniform(0.0,9.0,24))
marks = list(np.random.uniform(0.0,100.0,24))

# visualise data in histogram
mp.hist(hours_studied,10)
mp.show()

# calculate the necessary values 
slope,intercepts,r,p,std_error = st.linregress(hours_studied,marks)

# create a function to predict the values
def predict(x):

    y = slope * x + intercepts

    return y

# create a model that uses the function to predict the values
prediction_model = list(map(predict,hours_studied))


# performing visualization for linear regression
mp.scatter(hours_studied,marks)
mp.plot(hours_studied,prediction_model)
mp.show()

# use polynomial regression if the relationship ==0
if(r==0 or r < 1):
      
      polynomial_regression_model = np.poly1d(np.polyfit(hours_studied,marks,3))

      linespace = np.linspace(0,9,100)

      # performing visualization on polynormial
      mp.scatter(hours_studied,marks)
      mp.plot(linespace,polynomial_regression_model(linespace))
      mp.show()