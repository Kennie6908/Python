import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the data using data_name = pd.read_csv('filename.csv')

# to create a simple scatterplot, use sns.scatterplot(x = data_name['columnName'], y = data_name['columnName'])
# the method is sns.scatterplot()
# x and y arguments are the 2 columns that are being compared

# to add a regression line, simply do sns.scatterplot(same arguments), but change .scatterplot to .regplot.
# method becomes sns.regplot(with scatterplot arguments)

# to add color labeling based on a categorical variable, we can add a hue arguemnt.
# sns.scatterplot(hue = data_name['categorical columnName'])
# ex. if we compared hours studied and final score, then see which students (plot points) were honors students,
# we could use hue to quickly label if a student was honors or not (yes or no).

# to add regression lines, or multiple regression lines, use sns.lmplot()
# ARGUMENTS FOR LMPLOT() ARE DIFFERENT!
# LMPLOT AUTOMATICALLY CREATES A SCATTERPLOT!
# sns.lmplot(x = 'columnName', y = 'columnName', hue = 'categorical columnName', data = data_name)
# x and y do not need data_name['columnName'], only the 'columnName' is needed.
# hue is optional to graph different regression lines for the different hues (categories)
# data = the variable where the data is stored.

# also something called swarmplot, created by sns.swarmplot(x = data_name['columnName'], y = data_name['columnName'])
# used to compare a categorical variable with a numerical variable using scatterplots.
