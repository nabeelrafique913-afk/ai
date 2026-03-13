import pandas as pd

# Read csv file to DataFrame
#  Reference: https://pandas.pydata.org/docs/dev/reference/api/pandas.read_csv.html
#  Note below, date formatting - In Pandas, DateTime is a data type that represents a single point in time. It is especially useful when dealing with time-series data like stock prices, weather records, economic indicators etc.

df = pd.read_csv('nabeel/usstate.csv', delimiter=",",parse_dates=[2],date_format={'date_added': '%d-%m-%Y'})
print(df)

print('df -- types' , df.dtypes)
print('df -- info', df.info())

df['Valuation ($B)'] = (
    df['Valuation ($B)']
    .str.replace('$', '', regex=False)
    .str.replace('B', '', regex=False)
    .astype(float)
)
print(df.dtypes)
print('type:', df['Valuation ($B)'].dtype)

df.rename(columns={'Valuation ($B)' : 'Dollar'} ,inplace=True)
print(df)

second_1 = df['Dollar']
print(second_1)



# print last 9 rows 
print('last 9 nine rows')
print(df.tail(9))
print()

# print first 12 rows
print('first 12 rows')
print(df.head(12))
print()

# operate all statics 
print('print all statics opearation:',df.describe())

# find shape
print('row and column shape:' , df.shape)

# access one column
dollar = df['Dollar']
print('one column')
print(dollar)
"""
0      140.0
1      100.3
2       95.0
3       45.6
4       40.0
       ...
931      1.0
932      1.0
933      1.0
934      1.0
935      1.0"""


# access two column  date
dollar_Country = df[['Dollar' ,'Country']]
print('acces two columnn ')
print(dollar_Country)
print()
""" Dollar        Country
0     140.0          China
1     100.3  United States
2      95.0  United States
3      45.6         Sweden
4      40.0      Australia
..      ...            ...
931     1.0  United States
932     1.0  United States
933     1.0  United States
934     1.0  United States
935     1.0      Australia
"""
# all columns
all_column = df[['Company','Dollar','Date Joined','Country','City','Industry','Select Investors']]
print('all')
print(all_column) 
print()

"""
 Company  Dollar  ...                         Industry                                   Select Investors
0          Bytedance   140.0  ...          Artificial intelligence  Sequoia Capital China, SIG Asia Investments, S...     
1             SpaceX   100.3  ...                            Other  Founders Fund, Draper Fisher Jurvetson, Rothen...     
2             Stripe    95.0  ...                          Fintech        Khosla Ventures, LowercaseCapital, capitalG     
3             Klarna    45.6  ...                          Fintech  Institutional Venture Partners, Sequoia Capita...     
4              Canva    40.0  ...     Internet software & services  Sequoia Capital China, Blackbird Ventures, Mat...     
..               ...     ...  ...                              ...                                                ...     
931        YipitData     1.0  ...     Internet software & services  RRE Ventures+, Highland Capital Partners, The ...     
932         Anyscale     1.0  ...          Artificial Intelligence  Andreessen Horowitz, Intel Capital, Foundation...     
933  Iodine Software     1.0  ...      Data management & analytics  Advent International, Bain Capital Ventures, S...     
934       ReliaQuest     1.0  ...                    Cybersecurity              KKR, FTV Capital, Ten Eleven Ventures     
935       Pet Circle     1.0  ...  E-commerce & direct-to-consumer  Prysm Capital, Baillie Gifford & Co., TDM Grow...     
"""
# Case 1 : using .loc - default case - starts here
# Reference: https://www.datacamp.com/tutorial/loc-vs-iloc
# 
"""
Syntax               df.loc[row_indexer, column_indexer]              df.iloc[row_indexer, column_indexer]
Indexing Method      Label-based                                      Position-based indexing
Used for Reference   Row and column labels (names)                    Numerical indices of rows and columns (starting from 0)
"""
#Selecting a single row using .loc
second_1 = df.loc[6]
print('single  row')
print(second_1)
print()

# multiple row 
second_2 = df.loc[[5,8,200,90]]
print('multiple rows')
print(second_2)
print()

# select row and column 
second_3 = df.loc[5,'Date Joined']
print('row and column')
print(second_3)
print()

# slicing a rows 
second_4 = df.loc[5 :100]
print('slicing a rows:')
print(second_4)
print()

# slicing a columns 
second_5 = df.loc[:,'Company':'Industry']
print('slicing a columns:')
print(second_5)
print() 

second_6 = df.loc[df['Country'] == 'United States']
print(second_6)

second_7 = df.loc[5 , 'Select Investors']
print(second_7)

second_7 = df.loc[5:100 , 'Company':'Select Investors']
print(second_7)

conditional_1 = df.loc[df['Company'] ==  'Epic Games']
print(conditional_1)

conditional_2 = df.loc[df['Dollar'] .isin([25 , 15])]
print(conditional_2)

print(df['Date Joined'].dtype)

df['Date'] = pd.to_datetime(df['Date Joined'], errors='coerce')


conditional_3 = df[df['Date Joined'] == 12/30/2014]
print(conditional_3)


# slicing row with column

second_8 = df.loc[5:120, ['Company']]
print('row with column:')
print(second_8)
print()

second_9 = df.loc[8:600,['Select Investors']]
print("row with column")
print(second_9)
print()


second_10 = df.loc[[5,6],['Company','Select Investors']]
print('rows')
print(second_10)
print()


second_11= df.loc[5:800,['Company','Select Investors']]
print('rows')
print(second_11)


second_12 = df.loc[700:800,'Dollar':'Industry']
print('slicing rows and columns')
print(second_12)
print()

# combine rows and column using loc
second_13 = df.loc[df['Dollar'] == 25 , 'Dollar':'Industry']
print('combine rows and column')
print(second_13)
print()

id__1= df.loc[df['id'] == 5]
print(id__1)




# Case 1 : using .loc - default case - ends here

print("# Case 2 : using .loc with index_col - starts here")
# Case 2 : using .loc with index_col - starts here
# Second cycle - with index_col as company
# Why Second cycle - Note Index - , index_col=company

company_1 = df.loc[df['Company'] == 'Stripe']
print(company_1)

company_2 = df.loc[5:100, 'Company']
print(company_2)

company_3 = df['Company']
print(company_3)

