import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

data = pd.read_csv('matplotlib8.csv')

# changes all dates in date column from string to a datetime object
data['Date'] = pd.to_datetime(data['Date'])
# sorts the values in the date column
data = data.sort_values('Date')

price_date = data['Date']
price_close = data['Close']

# plot_date(x, y), use linestyle argument to make a solid line between points
plt.plot_date(price_date, price_close, linestyle = 'solid')

# .gcf gets current figure, use autoformat to format date appearance on x axis
plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()
