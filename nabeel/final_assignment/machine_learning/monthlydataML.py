import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('nabeel/machine_learning/monthlydataML.csv')
print(df)

print('info' , df.info())
print('null',df.isnull().sum())
print('type' , df.dtypes)
print('describe' , df.describe())
print('min' , df.min())
print('max', df.max())

print('len',len(df))
print('shape' , df.shape)

variables = ['Industrial_Production','Manufacturers_New_Orders: Durable Goods','Consumer_Price Index','Unemployment_Rate','Retail_Sales','Producer_Price_Index','Personal_Consumption_Expenditures','National_Home_Price_Index','All_Employees(Total_Nonfarm)','Labor_Force_Participation_Rate','Federal_Funds_Effective_Rate','Building_Permits','Money_Supply_(M2)','Personal_Income','Trade_Balance','Consumer_Sentiment','Consumer_Confidence']
for var in variables:
    sns.lineplot(x='Year' , y=var , data=df)
plt.show()

X = df[['Year','Month']]
y = df[['Industrial_Production','Manufacturers_New_Orders: Durable Goods','Consumer_Price Index','Unemployment_Rate','Retail_Sales','Producer_Price_Index','Personal_Consumption_Expenditures','National_Home_Price_Index','All_Employees(Total_Nonfarm)','Labor_Force_Participation_Rate','Federal_Funds_Effective_Rate','Building_Permits','Money_Supply_(M2)','Personal_Income','Trade_Balance','Consumer_Sentiment','Consumer_Confidence']]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X , y , 
                                                    test_size=0.2,
                                                    random_state=22)


print('shape' , X.shape)
print('y shape:',  y.shape)

from sklearn.linear_model import  LinearRegression
lr_model= LinearRegression()
lr_model.fit(X_train , y_train)

print('intercept:' ,lr_model.intercept_)
print('coef:' , lr_model.coef_)

feature_names = X.columns
model_coefficients = lr_model.coef_

import pandas as pd

# assume
targets = y.columns  # 17 target column names
features = X.columns  # 2 features: Year, Month
coefs = lr_model.coef_  # shape = (17, 2)

# Flatten to long format
data = []
for i, target in enumerate(targets):
    for j, feature in enumerate(features):
        data.append([target, feature, coefs[i, j]])

coefficients_df = pd.DataFrame(data, columns=['Target', 'Feature', 'Coefficient'])
print(coefficients_df)

y_pred = lr_model.predict(X_test)


# Convert predictions to DataFrame with same column names as y_test
y_pred_df = pd.DataFrame(y_pred, columns=y_test.columns, index=y_test.index)

# Optional: rename predicted columns to identify
y_pred_df.columns = [col + "_pred" for col in y_test.columns]

# Combine actual and predicted
results = pd.concat([y_test, y_pred_df], axis=1)

print("Actual vs Predicted.....\n", results.head())


from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')


actual_minus_predicted = np.sum((y_test - y_pred)**2)
actual_minus_actual_mean = np.sum((y_test - y_test.mean())**2)
r2 = 1 - actual_minus_predicted/actual_minus_actual_mean
print('R²:', r2)


print(" R2 also comes implemented by default into the score method of Scikit-Learn's linear regressor class...\n", lr_model.score(X_test, y_test))




