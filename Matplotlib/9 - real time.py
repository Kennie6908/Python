import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

# important import here is FuncAnimation
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

# create two empty arrays for x and y values
x_vals = []
y_vals = []

# uses itertools count function, which will just count up one number
index = count()

# animation function. Requires an i parameter, which stands for interval.
def animate(i):
    # appending values to our x and y arrays. next() just gets next item in iterator count, so ie. next number 1, 2, 3...
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))

    # plt.cla() means clear labels each plot, since we want to specify our own constant label from the start.
    plt.cla()
    plt.plot(x_vals, y_vals)

# actual animation call here
# call FuncAnimation object, with three parameters.
# FuncAnimation(figure name, animation name, interval in milliseconds)
# so plt.gcf() means get current figure --> figure name
# animate is our animation function that we created
# interval = 1000 means 1 second, so the animation will happen every second. 
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
plt.tight_layout()
plt.show()
