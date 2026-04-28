# import numpy
import numpy as np

# import sklearn for modeling
from sklearn import linear_model as lm

# import sk for scaling
from sklearn.preprocessing import StandardScaler as ss

# create an object of standard scaller
scale = ss()

# creating data randonly
studying_hours = np.random.uniform(0.0,9.0,24)
listening_in_class = np.random.uniform(0.0,9.0,24)
comple_activities = np.random.uniform(0.0,9.0,24)
sports = np.random.uniform(0.0,9.0,24)
grades_accumulated = np.random.uniform(0.0,9.0,24)

# listening the variables i want to use 
x = [['studying_hours','listening_in_class','comple_activities','sports']]
y = ['grades_accumulated']

# transform raw data
scaledX = scale.fit_transform(x)

# create a model used to predict
model = lm.LinearRegression()
model.fit(x,y)

# scale new data
scaled = scale.transform([[8.0,7.0]])

# predict
prediction = model.predict([scaled[0]])
print(prediction)

# find the coefficient
print(model.coef_)