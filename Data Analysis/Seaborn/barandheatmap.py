import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read data as always, and specify an index column if you need to
# data_name = pd.read_csv('filename.csv', index = 'columnName')

# to create a bar plot, use sns.barplot(x = data_name[columnName], y = data_name[columnName])
# the method is sns.barplot()
# x and y are the columns of the data that you want to plot
# if one of the columns you want to use is the index column, CANNOT USE [columnName] to select it!
# must use data_name.index to select the index column!


# to create a heatmap, use sns.heatmap(data = data_name, annot=True)
# the method is sns.heatmap()
# data = the variable where the data is stored

# annot = True displays the values in each cell of the heatmap.
# Setting it to false hides the values so all you see are the cell colors.
