import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('matplotlib6.csv')
ids = data['Responder_id']
ages = data['Age']

# x values
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# to plot histogram, use .hist(count (y) values, bin (x) values)
# arguments include edgecolor, log. Log changes y axis scale to 10^x (ex. 10^4).
# can use log = True when there is a large outlier to format data.
# there is also an plt.xlim(xmin = value, xmax = value) if necessary to limit the x values if desired
plt.hist(ages, bins= bins, edgecolor = 'black', log = True)

median_age = 29
color = '#fc4f30'

# can create a vertical line using .axvline (the v is for vertical).
# .axvline(value of the line, color, label...)
plt.axvline(median_age, color = color, label = 'Age Median')

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()
