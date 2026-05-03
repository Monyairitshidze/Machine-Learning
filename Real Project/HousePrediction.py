# import pandas to process data
import pandas as pd

# import stanard scaling
from sklearn.preprocessing import StandardScaler as ss

# use histogram to see data distribution
import matplotlib.pyplot as mplpp


# create storage to load data into our system
house_data = pd.read_csv("Housing.csv",header=0, sep=",")

# create a dataframe to structurer data well
df = pd.DataFrame(data= house_data)

# separte the varibales
x = df[['area'
        ,'bedrooms'
         ,'bathrooms'
          ,'stories'
           ,'mainroad'
            ,'guestroom'
             ,'basement'
              ,'hotwaterheating'
               ,'airconditioning'
                ,'parking'
                 ,'prefarea'
                  ,'furnishingstatus']]

# use only numeric data for hist
x_numeric = x.select_dtypes(include=['Int64','Float64'])

y = df['price']

# data preparation
# remove NAN values
df.dropna(axis=0, inplace=True)

# visualise data using histogram
mplpp.hist(x_numeric,bins=6)
mplpp.show()