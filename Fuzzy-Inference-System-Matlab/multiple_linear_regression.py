import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv("dataset.csv")
print(df)

reg = linear_model.LinearRegression()
# Defining data frames as below
reg.fit(df[['Daily customers','Electronics items','Groceries Items','Competition']],df.Sales)

# Printing the m values and b
print("m values:",reg.coef_)
print("b:",reg.intercept_)

test_input = [[5,5,50,9.5]]
result = reg.predict(test_input)
print(result)