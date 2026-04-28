# import numpy
import numpy as np

# import sklearn for modeling
from sklearn import linear_model as lm

# creating data randonly
studying_hours = np.random.uniform(0.0,9.0,24)
listening_in_class = np.random.uniform(0.0,9.0,24)
comple_activities = np.random.uniform(0.0,9.0,24)
sports = np.random.uniform(0.0,9.0,24)
grades_accumulated = np.random.uniform(0.0,9.0,24)

# listening the variables i want to use 
x = [['studying_hours','listening_in_class','comple_activities','sports']]
y = ['grades_accumulated']

# create a model used to predict
model = lm.LinearRegression()
model.fit(x,y)

prediction = model.predict([[8.0,7.0]])
print(prediction)

# find the coefficient
print(model.coef_)