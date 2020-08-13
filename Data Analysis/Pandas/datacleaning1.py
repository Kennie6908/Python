import numpy as np
import pandas as pd

# True if null, false if not null
# pd.isnull(np.nan) -->    outputs True
# pd.isnull(None) -->    outputs True

# True if not null, false if null
# pd.notnull(None) -->    outputs False
# pd.notnull(np.nan) -->   outputs False

# can use isnull and notnull on Series and DataFrames
# pd.isnull(pd.Series([1, np.nan, 7]))
# will print a series with index column and True/False column
# pd.isnull(pd.DataFrame...)
# will print a table with true and false values

# can use isnull or notnull.sum() to get count of all nulls
# ex. pd.notnull(pd.Series(...)).sum() returns count of non-null items

# to get rid of all null values, use .dropna()
# SERIES AND DATAFRAMES ARE NOT MUTABLE
# if pd.Series([...]).dropna() returns a table, pd.Series([]) is not changed!
# must store into a new variable... newSeries = pd.Series([]).dropna()

# to get data shape and info
# df = pd.DataFrame([...])
# df.shape() gives table size as tuple
# df.info() returns shape, datatype, non-null count in each column...

# .DROPNA() drops ENTIRE ROW with a null value
# to change this, use argument how = 'all' or how = 'any'
# default is 'any', 'all' will remove column if entire row is null
# can specify threshold using 'thresh' = a number, which will delete row if null count > that number
# ex. df.dropna(how = 'all') or ex. df.dropna(thresh = 3)

# to replace null values in a Series, use .fillna()
# .fillna(newvalue) replaces all null values with newvalue
# .fillna(method ='ffill') ffill means forward fill, which takes the previous value before null and changes null to that value
# .fillna(method = 'bfill') bfill means backward fill, which takes the value after the null and changes null to that value
# CAREFUL USING method = 'ffill' or 'bfill' since they can leave null values if null is at start or end of data

# to replace null values in a DataFrame, use .fillna() WITH AN AXIS
# axis = 0 means vertical, axis = 1 means horizontal
# ex. df.fillna(method = 'ffill', axis = 0)

# to count values of a Series or DataFrame, use .value_counts()
# ex. df['Type 1'].value_counts()
# returns the number of unique values in a column

# to replace values of a column, use .replace()
# ex. df['Type 1'].replace('Fire', 'Water')
# ex. df['Type 1'].replace({'Fire':'Water', 'Air':'Earth'})

# to fix errors based on a condition
# df.loc[df['Age'] > 100, 'Age'] = df.loc[df['Age'] > 100, 'Age'] / 10;
