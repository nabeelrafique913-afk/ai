import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data = pd.DataFrame({'x':np.arange(100) , 'y':np.random.rand(100).cumsum()})

sns.set_theme(style='dark')
sns.histplot(x='x' , y='y' ,data=data)
plt.show()

sns.set_theme(style='darkgrid')
sns.kdeplot(x='x' , y='y' , data=data)
plt.show()

sns.set_theme(style='whitegrid')
sns.barplot(x='x' , y='y' , data=data)
plt.show


df = pd.read_csv('nabeel/fooddata.csv' , delimiter=',' , index_col='address' )

print(df.dtypes)
head = df.head(100)
head1 = df.head(1002)
print(head)
print(head1)

sns.set_theme(style='darkgrid', rc={'axes.facecolor' : 'blue' , 'grid.color' : 'green'})
g=sns.displot(data=head, x='name' , y='postalCode' ,hue='name')
g.figure.suptitle("sns.displot, data=head , x = name , y = postalcode , hue = name")

sns.set_theme(style='darkgrid')
g=sns.boxplot(data=head, x='name' , y='postalCode' ,hue='name')
g.figure.suptitle("sns.boxplot, data=head , x = name , y = postalcode , hue = name")

sns.set_theme(style='white')
g=sns.boxenplot(data=head , x='city' , y='address')
g.figure.suptitle("sns.boxenplot, data=head , x=city, y=address")

sns.set_theme(style='darkgrid')
g=sns.catplot(data=head , x='websites' , y='city' , hue='city')
g.figure.suptitle("sns.catplot, data=head , x=website , y = city")

sns.set_theme(style='white')
g=sns.barplot(data=head , x='postalCode', y='city' ,hue='name')
g.figure.suptitle("sns.barplot, data=head , x=postalcode , y=name, hue=name")







