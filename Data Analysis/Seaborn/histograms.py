import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read the data first
# data_name = pd.read_csv('filename.csv')

# to create a histogram, use the sns.displot(a = data_name['columnName'], kde = False)
# a = the columnName that we want to plot
# kde = True or False draws a line that fits the curve of the data

# a smoothed histogram (just the curved line) is called a kernal density estimate (KDE)
# to create one, use sns.kdeplot(data = data_name['columnName'], shade = True)
# data = the variable that the data is stored --> columnName
# shade = True or False shades the area under the smoothed histogram.

# to create a 2D KDE, where one KDE is on top, and the other KDE is on the right, and there is a
# heatmap/spot area in the middle, use .joinplot()
# sns.joinplot(x = data_name['columnName'], y = data_name['columnName'], kind = "kde")
# specify the x and y columns
# kind = "kde" tells us to use kde graphs on the top and right. Can also do histograms...

# to color code graphs, just plot multiple displots or kdeplots and add label = 'label' in the arguments.
# plots will automatically color code if plotted on the same figure. 
# to add a legend for the labels, use plt.legend()
