import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('nabeel/machine_learning/medical_student.csv')
print(df)

print('info', df.info())
print('null',df.isnull())

# Columns jisme commas hain
cols = ['Female Doctors','Male Doctors','Total Doctors',
        'Female Dentists','Total Dentists']

# Comma remove aur int me convert
for col in cols:
    df[col] = df[col].str.replace(',', '').astype(int)

print(df.dtypes)  
print(df.head())

import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))
plt.plot(df['Years'], df['Total Doctors'], marker='o', label='Total Doctors')
plt.plot(df['Years'], df['Total Dentists'], marker='o', label='Total Dentists')
plt.xlabel("Year")
plt.ylabel("Number")
plt.title("Total Doctors & Dentists over Years")
plt.legend()
plt.grid(True)
plt.show()

from sklearn.model_selection import train_test_split

X = df[['Years','Female Doctors','Male Doctors']]  # features
y = df['Total Doctors']  # target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

from sklearn.model_selection import train_test_split

X = df[['Years','Female Doctors','Male Doctors']]  # features
y = df['Total Doctors']  # target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))


import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.scatter(X_test['Years'], y_test, color='blue', label='Actual')
plt.scatter(X_test['Years'], y_pred, color='red', label='Predicted')
plt.xlabel("Year")
plt.ylabel("Total Doctors")
plt.title("Actual vs Predicted Total Doctors")
plt.legend()
plt.show()

