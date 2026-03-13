#this is the final assesment of our course

#importing the different extternal libaries and packages 

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# redaing the data from the data set 
df= pd.read_csv('nabeel/final_assignment/InsuranceData.csv')
print(df)

#lets take firt 5 values of data 
print(df.head(5))
#finfing the last 5 rows
print(df.tail(5))

#reationship between the different variables through graph 
df.plot.scatter(x='bmi',y='charges',title='scattere plot between two coloumn');
plt.show()

# applying the all statical operations on the data
print(df.describe())

#for finding the correlation  and to apply all  the machine leraning operations  we need to covert some text coloumn into numbers because machine learning only understansd numbers 

df['sex'] = df['sex'].map({'female':0,'male':1})
df['smoker'] = df['smoker'].map({'no':0,'yes':1})
df = pd.get_dummies(df, columns=['region'])

#now we are finding the correlation between the data 
print(df.corr())

#converting the data into  input and output lables
X = df[['age','sex','bmi','children','smoker',
        'region_northeast','region_northwest','region_southeast', 'region_southwest']]
y = df['charges']

#applying the actual Machine learning 
from sklearn.model_selection import train_test_split
#seperating the data into tran test spllit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#importing the model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score
#create a model 
model=LinearRegression()
#for training of model
model.fit(X_train,y_train)
#making a prediction
y_pred = model.predict(X_test)

#finding the result on model
mean = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Absolute Error:", mean)
print("R2 Score:", r2)

#applying the regression model
from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor()
dt.fit(X_train, y_train)
pred_dt = dt.predict(X_test)
print("decision tree R2 Score", r2_score(y_test, pred_dt))
#applying the random forests
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
pred_rf = rf.predict(X_test)
print("random forest R2 Score", r2_score(y_test, pred_rf))
#applying the Gardient boost regressor
from sklearn.ensemble import GradientBoostingRegressor
gb = GradientBoostingRegressor()
gb.fit(X_train, y_train)
pred_gb = gb.predict(X_test)
print("Gradient Boosting R2 Score:", r2_score(y_test, pred_gb))

#result
#so the gardient boost model is best
