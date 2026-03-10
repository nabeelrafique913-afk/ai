import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('nabeel/final_assignment/smoker_data.csv' )
print(df)

import seaborn as sns

sns.regplot(x='age' , y='charges' , data=df);
plt.show()

x=input('y6h7h')


X = df[['age','sex','bmi','children','smoker','region']]
y = df['charges']

SEED = 42

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)

print(X_train)
print(y_train)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

print(regressor.coef_)

age = regressor.predict([[9.5]])
print(age)
