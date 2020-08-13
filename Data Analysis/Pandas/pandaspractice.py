# import statement
import pandas as pd

# importing data into pandas
df = pd.read_csv('pandasdataset.csv')
# if you don't want the first index row, use pd.read_csv('filename.csv', index_col = 0)

# get first five rows
# print(df.head(5))

# get last five rows
# print(df.tail(5))

# print headers
# print(df.columns)

# to create a DataFrame
# pd.DataFrame({'columnName': [values], 'secondcolumn': [values]}, index = ['row name', 'row name'])

# to create a Series
# pd.Series(['list1', 'list2', 'list3', 'list4'...], index = ['rowname', 'rowname'...], name = 'Name of Series')

# read specific column, first 5 objects
# print(df['columnheader', 'anothercolumn'][0:5])

# read specific row (row 1)
# print(df.iloc[1])

# read specific location (Row, Column) --> ex. gets 3rd row 2nd column
# print (df.iloc[2,1])

# to iterate through rows
# for index, row in df.iterrows():
    # print (index, row['Name'])

# use loc when using specific criteria
# ex. df.loc[df['Type 1'] == 'Fire']
# this looks through type 1 row and only locates those with fire value

# to print count, median, mean, standard deviations, and max/mins
# df.describe()

# to sort values alphabetically or numerically
# df.sort_values('columnName', ascending = True or False)
# automatically sorts by lowest

# to sort multiple columns
# df.sort_values(['columnName', 'anotherColumn'], ascending = [0,1])
# MUST HAVE Ascending/Descending values for each column of sort.
# 0 equals false. 1 equals true.

# to add a column
# df['newColumnName'] = something...
# ex. df['total'] = df['attack'] + df['defense'] + df['hp']...
# ex. df['total'] = df.iloc[:, 4:10].sum(axis = 1)
    # takes horizontal sum of 1 column, 4th to 9th row, axis of 1 = horizontal, axis of 0 = vertical

# to remove a column
# df = df.drop(columns = ['columnName'])

# to output csv
# df.to_csv('newfilename.csv')
# to get rid of index column, include index = False
# ex. df.to_csv('newfilename.csv', index = False)

# to output to excel
# df.to_excel('newfilename.xlsx', index = False)


# to filter data, use loc with a condition
# df.loc[df['Type 1'] == 'Grass']
# locates grass types in type 1 column

# can add conditions using & (and)  | (or)    --> just make sure to include parentheses around all arguments
# can use > < >= <=

# can assign to a variable to create new DataFrame and keep original code untouched
# ex. new_df = df.loc[df['Type 1'] == 'Grass']

# filter can also use str.contains to search for keywords in columns
# ex. df.loc(~df['Name'].str.contains('Mega'))
# ~ means NOT. IT IS NOT THE EXCLAMATION POINT

# to get all unique values, use .unique()

# can also use regex using import re, then regex = True argument
# ex. df.loc[df['Name'].str.contains('^pi[a-z]*'), flags = re.I, regex = True]
# looks for all names that contains pi.....   flags used to ignore case, regex = True allows regex to be used

# to change things based on conditions
# df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
# locates all 'fire' in the Type 1 column, then changes those located in the type 1 column to flamer.
# the second 'type 1' is a parameter that tells us where we should change things
# ex. df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
# locates all fire types in type 1 column, then looks at the legendary column from the parameter and changes those located to true. Will give true to legendary to all fire types.

# can modify multiple columns at a time
# df.loc[df['total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']

# aggregate stats using groupby
# ex. df.groupby(['Type 1']).mean().sort_values('Defense', ascending = False
# groups all the different type 1s, gets their means, sorts the values by highest to lowest defense

# ex. df.groupby(['Type 1'].count())
# will return counts for how many pokemon are a certain type
# will return this count in all columns
# to avoid this, create a new column df['newcolumn'] = something
# then do df.groupby(['Type 1'].count()['newcolumn']), which will ouput only the newcolumn with the counts

# can group by multiple conditions at same groupby
# ex. df.groupby(['Type 1', 'Type 2'].count()['newcolumn'])

# to rename columns, use .rename(columns = {'oldname':'newname', 'oldname':'newname'...})

# to rename index columns, use .rename_axis('newname', axis = "rows" or "columns")

# to combine two DataFrames by adding its rows under the other, use .concat()
# pd.concat(['first DF', 'secondDF'])

# to combine the columns of two DataFrames, use .join('other dataframe')
# must have matching index values which will be the first column of the resulting join (this is the column they have similar values for)
# can create matching index values by using .set_index('common row')
# ex. df.set_index('key').join(other.set_index('key'))

# USE .CONCAT to just add rows to the bottom of dataframe, USE .JOIN to add columns from another dataframe if both have a similar column in common
