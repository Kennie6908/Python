import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

# a list of dates created using datetime, from built in python library
dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

# y values
y = [0, 1, 3, 4, 6, 5, 7]

# plot_date(x, y), use linestyle argument to make a solid line between points
plt.plot_date(dates, y, linestyle = 'solid')

# .gcf gets current figure, use autoformat to format date appearance on x axis
plt.gcf().autofmt_xdate()

# to format date using matplotlib dates module
# call the module mpl_dates .DateFormatter( format here )
date_format = mpl_dates.DateFormatter('%b %d, %Y')
# .gca() = get current axis. gets the xaxis, uses .set_major_formatter to get the formatted date
plt.gca().xaxis.set_major_formatter(date_format)
# outputs month day, year from ('%b %d, %Y')

plt.tight_layout()

plt.show()
