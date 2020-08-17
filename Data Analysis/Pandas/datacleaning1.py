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

# can use isnull or notnull.sum() to get count of all nulls in a column
# ex. pd.notnull(pd.DataFrame(...)).sum() returns count of non-null items
# will return a list of the number of null values in each column 

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

# to drop entire column with a null value, use .dropna(axis = 1)

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

# to find duplicates, we can use dataframename.duplicated()
# this will return a true or false value for each row
# CAREFUl! This will not return false for duplicates that are the first instance (top down).
# ex. if there are three duplicates, the first will be false (since it is first instance), then the others will be true.

# to fix this, use .duplicated(keep = False)
# this will remove all duplicates, no matter if they are the first instance.

# to get rid of all duplicates from a Series or Dataframe, use dataframename.drop_duplicates()
# same rules apply as .duplicated(), the first instance of an element will not be considered a duplicate
# to get rid of all duplicates, use .drop_duplicates(keep = False)

# .duplicated() and .drop_duplicates() look at each entire row to see if values are duplicated with another row.
# if you don't want the entire row to be checked, but just a certain column of values, use subset argument.
# ex. dataframename.duplicates(subset=['columnName'])

# to clean columns, first get your column.
# df['columnName']
# then convert to whatever data type you want to work with. .str for string, .dt for date, .cat for category.
# df['columnName'].str --> this gets all the values to a string.

# str methods include .contains(), .split(), .replace()

# str.split('value to split by') splits the input string into a list of individual values.
# can use str.split('value to split by', expand = True) to create a dataFrame out of the resulting split list.

# str.contains('value to look for') looks for that value inside an string.
# returns a list of booleans if that value is inside the input string.

# str.replace('value to look for', 'value to replace with')
# looks for a given value and replaces it with a given value.
# can be used to get rid of spaces easily --> str.replace(" ", "")

# to normalize data distribution (make it a normal distribution)
# use from scipy import stats
# use boxcox, look up documentation later

# to scale data, use scaleddata = minmax_scaling(original_data, columns = ['columnname'])
# this will scale data from a range of 0 to 1, which can make working with large numbers easier


# working with dates
# first, check data type using df['columnname].dtype
# if result = o --> it is an object and not a date
# to get the object into a date, use the pd.to_datetime(df['columnname of dates'], format = "%m%d%Y")
# for formatting, %m means month, %d means days, %y means two digit year, %Y means four digit year. Can edit formatting by changing order, adding commas/dashes in between...

# to select the day from a datetime object, use df['columnname'].dt.day or datetimeobject.dt.day



# dealing with encoding problems
# always use utf-8 with pandas! 
# to encode to utf-8, use dataframename.encode()
# to decode something that isn't utf-8, use dataframename.decode('type of encoding'), then use .encode('utf-8')
# to read a csv file in a different encoding, use pd.read_csv('filename', encoding = 'whatever encoding it is in')

# to determine the encoding of a file, use this: 
# import chardet
# with open("filename.csv", 'rb') as rawdata:
#    result = chardet.detect(rawdata.read(number of lines - usually a large amount))
# print(result)
# this will print out the type of encoding, as well as the level of confidence. 
# after this, use .read_csv('filename.csv', encoding = 'whatever the result was')

# to save in utf-8, just use dataframename.to_csv('file name'). to_csv automatically uses utf-8. 


# working with string formatting
# .str.lower() changes the string to lower case
# .str.strip() removes all whitespace before and after the string, so we are just left with the word
# to find strings that are very similar to another given string, use fuzzywuzzy. 
# import fuzzywuzzy
# from fuzzywuzzy import process

# matches = fuzzywuzzy.process.extract("usa", countries, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
# this saves a list of matches that are close to the given string "usa" in a countries list, with a limit of the 10 closest matches. 
# Uses the scorer fuzzywuzzy.fuzz.token_sort_ratio, which returns a table with the first column being values, and the second column being a number from 0 - 100, with 100 being the closest match. 
# Must use a for loop with matches[0] to get the value, and matches[1] to get the ratio score. 

# then use rows_with_matches = df[column].isin(matches) to get row number of matches
# df.loc[rows_with_matches, columnname] = string_to_match to find the row of matches, and replace them with the correct value