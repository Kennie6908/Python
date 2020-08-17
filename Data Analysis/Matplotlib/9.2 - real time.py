import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

# important import statement here
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

# animate function
def animate(i):

    # using pandas to read csv.
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    # clearing our labels each time we plot
    plt.cla()
    plt.plot(x, y1, label = 'Channel 1')
    plt.plot(x, y2, label = 'Channel 2')

    # specifing legend position every time we plot, otherwise it might change with new data.
    plt.legend(loc = 'upper left')

    # same thing here, auto adjusting padding after each plot, since data might change.
    plt.tight_layout()

# creating our animation with FuncAnimation object.
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.show()
