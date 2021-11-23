import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv("dataset.csv")
print(df)

reg = linear_model.LinearRegression()
# Defining data frames as below
reg.fit(df[['Daily customers','Electronics items','Groceries Items','Competition']],df.Sales)

# Printing the m values and b
print(reg.coef_)
print(reg.intercept_)