import pandas as pd

# Read csv file to DataFrame
#  Reference: https://pandas.pydata.org/docs/dev/reference/api/pandas.read_csv.html
#  Note below, date formatting - In Pandas, DateTime is a data type that represents a single point in time. It is especially useful when dealing with time-series data like stock prices, weather records, economic indicators etc.

df = pd.read_csv('nabeel/fooddata.csv', delimiter=",",parse_dates=[9],date_format={'date_added': '%d-%m-%Y'})

df = df.assign(new_column='NABEEL')

# Declare a list that is to be converted into a column
#address_1 = ['NewYork', 'Chicago', 'Boston', 'Miami']

# Using 'Address_1' as the column name
# and equating it to the list
#df['Address_1'] = address_1


print(df)
print('df - datatype:',df.dtypes)
print('df-info:',df.info())

# diplay last 10 rows
print('last ten rows')
print(df.tail(10))
print()

# display first ten rows
print('first ten rows')
print(df.head(10))
print()

# apply all statics operation 
print('apply all statics operation:',df.describe())

# find rows and colum
print('rows and colum:',df.shape)
print()

# acess the colum
address = df['address']
print('acess the colum:')
print(address)
print()
""""
0                 324 Main St
1             530 Clinton Ave
2        408 Market Square Dr
3       6098 State Highway 37
4             139 Columbus Rd
                ...
9995    3013 Peach Orchard Rd
9996        678 Northwest Hwy
9997             1708 Main St
9998        67740 Highway 111
9999      5701 E La Palma Ave"""

# acess 2 colum
colum_2 = df[['address', 'city']]
print('acess 2 colum:')
print(colum_2)
print()

"""
  address                    city
0               324 Main St                 Massena
1           530 Clinton Ave  Washington Court House
2      408 Market Square Dr               Maysville
3     6098 State Highway 37                 Massena
4           139 Columbus Rd                  Athens
...                     ...                     ...
9995  3013 Peach Orchard Rd                 Augusta
9996      678 Northwest Hwy                    Cary
9997           1708 Main St                Longmont
9998      67740 Highway 111          Cathedral City
9999    5701 E La Palma Ave                 Anaheim"""

# acess multiple colum
multiple_colum = df[['country','keys','latitude','longitude','name']]
print('acess multiple colum:')
print(multiple_colum)
print()

"""
0         US                us/ny/massena/324mainst/-1161002137  44.921300  -74.890210                   McDonald's       
1         US  us/oh/washingtoncourthouse/530clintonave/-7914...  39.532550  -83.445260                      Wendy's       
2         US       us/ky/maysville/408marketsquaredr/1051460804  38.627360  -83.791410             Frisch's Big Boy       
3         US       us/ny/massena/6098statehighway37/-1161002137  44.950080  -74.845530                   McDonald's       
4         US               us/oh/athens/139columbusrd/990890980  39.351550  -82.097280              OMG! Rotisserie       
...      ...                                                ...        ...         ...                          ...       
9995      US        us/ga/augusta/3013peachorchardrd/-791445730  33.415257  -82.024531                      Wendy's       
9996      US               us/il/cary/678northwesthwy/787691191  42.217300  -88.255800  Lee's Oriental Martial Arts       
9997      US               us/co/longmont/1708mainst/-448666054  40.189190 -105.101720                    Five Guys       
9998      US     us/ca/cathedralcity/67740highway111/-981164808  33.788640 -116.482150                El Pollo Loco       
9999      US            us/ca/anaheim/5701elapalmaave/554191587  33.860074 -117.789762                   Carl's Jr."""    

"""There are four primary ways to select rows with .loc. These include:
Selecting a single row
Selecting multiple rows
Selecting a slice of rows
Conditional row selection"""

# Case 1 : using .loc - default case - starts here
# Reference: https://www.datacamp.com/tutorial/loc-vs-iloc
# 
"""
Syntax               df.loc[row_indexer, column_indexer]              df.iloc[row_indexer, column_indexer]
Indexing Method      Label-based                                      Position-based indexing
Used for Reference   Row and column labels (names)                    Numerical indices of rows and columns (starting from 0)
"""
#Selecting a single row using .loc

secondrow_1 = df.loc[5]
print('Selecting a single row using .loc')
print(secondrow_1)
print()

# selecting a multiple rows using .loc
secondrow_2 = df.loc[[5,9]]
print('selecting a multiple rows using loc:')
print(secondrow_2)
print()

# selecting a slice rows using loc
secondrow_3 = df.loc[5:12]
print('slice  rows:')
print(secondrow_3)
print()

#Conditional selection of rows using .loc
secondrow_4 = df.loc[df['address']== '4182 Tonya Trl']
print('conditional rows:')
print(secondrow_4)
print()

conditional_2 = df.loc[df['latitude'] == 39.86969]
print('conditional row 2')
print(conditional_2)
print()

conditional_3 = df.loc[df['keys'] == 'us/ar/sheridan/613wcenterst/1780593795']
print('conditional_3')
print(conditional_3)
print()

conditional_4 = df.loc[df['latitude'] . isin([33.91335 , 43.83563])]
print('conditional4 .loc')
print(conditional_4)
print()

conditional_7 = df.loc[df['longitude'] == -83.79141]
print('conditional_7')
print(conditional_7)
print()

# slicing a singal colum
secondrow_5 = df.loc[5:10 , ['keys']]
print('slicing a singal colum using loc:')
print(secondrow_5)
print()

# slicing a multiple colums using loc
secondrow_6= df.loc[9:4500 , ['keys' , 'longitude']]
print('multiple colum:')
print(secondrow_6)
print()


# slicing a multiple colum using loc
secondrow_7 = df.loc[0:5000 ,['address','city','country','keys','latitude','longitude','name','postalCode','province','websites']]
print('multiple colums:')
print(secondrow_7)
print()

# selecting a slice colum using .loc
secondrow_8 = df.loc[5:5205 , 'keys' : 'province']
print('selecting a slice colum using .loc')
print(secondrow_8)
print()

#Combined row and column selection using .loc
secondrow_9 = df.loc[df['latitude'] == 39.53255 , 'address' : 'keys']
print('Combined row and column selection using .loc')
print(secondrow_9)
print()

# Case 1 : using .loc - default case - ends here

print("# Case 2 : using .loc with index_col - starts here")
# Case 2 : using .loc with index_col - starts here
# Second cycle - with index_col as address
# Why Second cycle - Note Index - , index_col=address

df_index_col =pd.read_csv('nabeel/fooddata.csv',delimiter = ",", parse_dates=[5], date_format={'date_added': '%d-%m-%Y'} , index_col='address')
print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
# Second cycle - with index_col as address
print(df_index_col.loc['324 Main St'])
#selecting a singal row
secondrow = df_index_col.loc['5812 NW Expressway']
print('selecting row singal row')
print(secondrow)
print()

# selecting a multiple row using .loc
secondrow_1 = df_index_col.loc[['908 Padre Blvd' , '1313 S Wolfe Rd']]
print('selecting a multiple row using .loc')
print(secondrow_1)
print()

# selecting a slice using .loc
secondrow_2 = df_index_col.loc['2207 Highway 67 S' : '293 Social St']
print('selecting a slice using .loc')
print(secondrow_2)
print()

#Conditional selection of rows using .loc
secondrow_3 = df_index_col.loc[df_index_col['country'] == 'US']
print('Conditional selection of rows using .loc')
print(secondrow_3)
print()

conditional_2 = df_index_col.loc[df_index_col['keys']  == 'us/oh/hamilton/4182tonyatrl/-1055723171']
print('Conditional selection of rows using .loc')
print(conditional_2)
print()

#Selecting a single column using .loc
secondrow_4 = df_index_col.loc[:'2711 W. Kings Highway Ste. 18'  , ['longitude']]
print('Selecting a single column using .loc')
print(secondrow_4)
print()

#Selecting a single column using .loc

secondrow_5 = df_index_col.loc[:'2501 W Memorial Rd' , ['province','websites']] 
print('Selecting a single column using .loc')
print(secondrow_5)
print()

#Selecting a slice of columns using .loc

secondrow_6 = df_index_col.loc['1535 NW 50th St': '17520 Yorba Linda Blvd' ,'address' : 'websites']
print('Selecting a slice of columns using .loc')
print(secondrow_6)
print()

# #Combined row and column selection using .loc
# second_row8 = df_index_col.loc[df_index_col['acre_lot']==0.09,'price':'zip_code']
# print('Combined row and column selection using .loc')
# print(second_row8)
# print()

# Case 2 : using .loc with index_col  -  ends here

print("# Case 3 : Using .iloc - starts here")
# Case 3 : Using .iloc - starts here

"""Using .iloc: Selection by Integer Position
.iloc selects by position instead of label. This is the standard syntax of using .iloc: df.iloc[row_indexer, column_indexer]. There are two special things to look out for:

Counting starting at 0: The first row and column have the index 0, the second one index 1, etc.
Exclusivity of range end value: When using a slice, the row or column specified behind the colon is not included in the selection."""

#Selecting a single row using .iloc

secondrow = df_index_col.iloc[1]
print('Selecting a single row using .iloc')
print(secondrow)
print()

#selecting a multiple rows using .iloc
secondrow_1 = df_index_col.iloc[[1 , 9 ,5025]]
print('selecting a multiple rows using .iloc')
print(secondrow_1)
print()

# selecting a slice of rows using iloc
secondrow_2 = df_index_col.iloc[5:2500]
print('selecting a slice of rows using iloc')
print(secondrow_2)
print()

#selecting a  single colum using iloc
secondrow_4 = df_index_col.iloc[: , 3]
print('selecting a  single colum using iloc')
print(secondrow_4)
print()

# selecting a multiple colum using .iloc
secondrow_5 = df_index_col.iloc[: , [5 , 8]]
print('selecting a multiple colum using .iloc')
print(secondrow_5)
print()


#selecting a multiple colum using .iloc
secondrow_0 = df_index_col.iloc[:5 , [5 , 2]]
print('selecting a multiple colum using .iloc')
print(secondrow_0)
print()

#Selecting a slice of columns using .iloc
secondrow_6 = df_index_col.iloc[: , 0:6]
print('#Selecting a slice of columns using .iloc')
print(secondrow_6)
print()

#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("Combined row and column selection using .iloc")
print(second_row8)
print()

#Combined row and column selection using .iloc
second_row9 = df_index_col.iloc[2:2500,[1,3,7]]
print("Combined row and column selection using .iloc")
print(second_row9)
print()

# Case 3 : Using .iloc - ends here

# Next Run 
print("Next Run")

""""Pandas DataFrame Manipulation
DataFrame manipulation in Pandas involves editing and modifying existing DataFrames. Some common DataFrame manipulation operations are:

Adding rows/columns
Removing rows/columns
Renaming rows/columns"""

#Add a New Row to a Pandas DataFrame
# add a new row
# Copy array from list and add to DataFrame

df.loc[len(df.index)]=  ['758 Main St','Massena','US','us/ny/massena/324mainst/-1161002137',44.9213,-74.89021,'McDonalds',13662,'NY',"http://mcdonalds.com,http://www.mcdonalds.com/?cid=RF:YXT_FM:TP::Yext:Referra"]
print("Modified DataFrame - add a new row:")
print(df)
print()


#Remove Rows/Columns from a Pandas DataFrame


# delete row
df.drop( 1 ,axis=0 , inplace=True)
# delete row with index
df.drop(index=5 , inplace=True)
# delete rows with index
df.drop([3, 6], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)

# delete colum 
df.drop('address' ,axis=1 ,inplace=True)
# delete colum 
df.drop(columns='websites' , inplace=True)
# delete multiple colum
df.drop([ 'longitude' , 'name'] , axis=1 ,inplace=True)
# modify data frame after deleting colum
print('data frame after delete ,city,country,keys,latitude,postalCode,province')
print(df)
print()

#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns= {'city' : 'city__1'},inplace=True)
# rename colum
df.rename(mapper={'country' : 'pakitan', 'latitude': 'attitude'}, axis=1 , inplace=True)
print('rename labels')
print(df)
print() 

#Example: Rename Row Labels
# rename column one index label
df.rename(index={1: 7}, inplace=True)
# rename columns multiple index labels
df.rename(mapper={6: 10, 9998: 100}, axis=0, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame - Rename Row - 1 >>> 7 , 6 >>> 10 , 9998 >>> 100  Labels:")
print(df)

#query() to Select Data
#The query() method in Pandas allows you to select data using a more SQL-like syntax.

# select the rows where the age is greater than 25
# selected_rows = df.query('price == \'bed\' or acre_lot > 12365')
# print(selected_rows.to_string())
# print(len(selected_rows))

# sort DataFrame by price in ascending order
sort_1 = df.sort_values(by='keys')
print(sort_1.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)
df1 = df.sort_values(by=['attitude' , 'postalCode'])
print('sorting valus')
print(df1.to_string(index=False))
print()

"""
Reference: https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/
Explanation: This code creates a DataFrame from a dictionary with three columns (Weight, Name, Age), structures it into a tabular format using pd.DataFrame() and converts it into a fully visible string representation with df.to_string().

Syntax
DataFrame.to_string(buf=None, columns=None, col_space=None, header=True, index=True, na_rep=’NaN’, formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal=’.’, line_width=None)


Parameters:

buf: Buffer to write the output string to (e.g., a file). Defaults to None, which means the output is returned as a string.
columns: Specifies a subset of columns to include in the output. If None, all columns are printed.
col_space: Defines the minimum width of each column.
header: Whether to print column names. Can also accept a list of column name aliases.
index: Whether to include index labels. Default is True.
na_rep: String representation for missing values (NaN). Default is ‘NaN’.
formatters: Dictionary or list of functions to apply to columns for formatting their output.
float_format: Formatter function to apply specifically to floating-point numbers.
sparsify: Controls hierarchical index formatting. If False, prints every multi-index key at each row.
index_names: Whether to print index names. Default is True.
justify: Alignment of column headers (‘left’, ‘right’, ‘center’, ‘justify’ or ‘justify-all’).
max_rows: Maximum number of rows to display. If exceeded, truncates output.
max_cols: Maximum number of columns to display. If exceeded, truncates output.
show_dimensions: If True, displays the shape (rows x columns) of the DataFrame.
decimal: Specifies the character for decimal separation (e.g., ‘,’ for European formatting).
line_width: Defines the maximum character width of a row before wrapping text."""

#Pandas groupby
#In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.

# group the DataFrame by the location_id column and
# calculate the sum of price for each category

group_by = df.groupby('attitude')['province'].sum()
print(group_by.to_string())
print('group_by:',len(group_by))
print()

""""Pandas Data Cleaning
Data cleaning means fixing and organizing messy data. Pandas offers a wide range of tools and functions to help us clean and preprocess our data effectively.
"""
# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print('cleaned:',df_cleaned)
print()

# filling NaN values with 0
df.fillna(143, inplace=True)

print("\nData after filling NaN with 143:\n", df)

# create a list named data
data = [2, 4, 6, 8 , 10 , 52]
# create Pandas array using data
array1 = pd.array(data)
print(array1)

"""<IntegerArray>
[2, 4, 6, 8, 10, 52]
Length: 6, dtype: Int64"""

# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5, 58, 69], dtype='int')
print(int_array)
print()

#Pandas Reshape
#In Pandas, reshaping data refers to the process of converting a DataFrame from one format to another for better data visualization and analysis.
#Pandas provides multiple methods like pivot(), pivot_table(), stack(), unstack() and melt() to reshape data. We can choose the method based on our analysis requirement.


# to be continued....















