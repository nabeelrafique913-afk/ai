import pandas as pd
import numpy as np

df = pd.read_csv('scraping/nabeelML/tradingdata.csv')

print(df)

print('types',df.dtypes)
print('null' , df.isnull().sum())
print(df.info())
print('describe' , df.describe())
print('mean' , df.mean())
print('min' ,df.min())
print('max' , df.max())

print('head' , df.head())

import seaborn as sns
import matplotlib.pyplot as plt

sns.lineplot(x='fuel_consumption' , y='eco_score' ,data=df)
plt.show()

variables = ['rpm_variation','harsh_braking_count','idling_time','fuel_consumption','acceleration_smoothness']
for var in variables:
 sns.lineplot(x=var , y='eco_score' , data=df)
 plt.show()

a = input('a')



print('corr' , df.corr())

from sklearn.model_selection import train_test_split

X = df[['rpm_variation','harsh_braking_count','idling_time',
      'fuel_consumption','acceleration_smoothness']]
y = df['eco_score']

print("X.shape :     \n", X.shape ) 
print("y.shape :     \n", y.shape ) 


SEED = 200
#After setting our X and y sets, we can divide our data into train and test sets. We will be using the same seed and 20% of our data for training:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.8, 
                                                    random_state=SEED)

#After splitting the data, we can train our multiple regression model. Notice that now there is no need to reshape our X data, once it already has more than one dimension:
print("X.shape :     \n", X.shape )   


#To train our model we can execute the same code as before, and use the fit() method of the LinearRegression class:

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

#After fitting the model and finding our optimal solution, we can also look at the intercept:
print("regressor.intercept_......\n", regressor.intercept_)

#And at the coefficients of the features
print("regressor.coef_ " , regressor.coef_)

feature_names = X.columns
model_coefficients = regressor.coef_

coefficients_df = pd.DataFrame(data = model_coefficients, 
                              index = feature_names, 
                              columns = ['Coefficient value'])
print(coefficients_df)


#In the same way we had done for the simple regression model, let's predict with the test data:
y_pred = regressor.predict(X_test)

results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("Actual vs Predicted.....\n" , results)


from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')



""""To dig further into what is happening to our model, we can look at a metric that measures the model in a different way, it doesn't consider our individual data values such as MSE, RMSE and MAE, but takes a more general approach to the error, the R2:"""
actual_minus_predicted = sum((y_test - y_pred)**2)
actual_minus_actual_mean = sum((y_test - y_test.mean())**2)
r2 = 1 - actual_minus_predicted/actual_minus_actual_mean
print('R²:', r2)




