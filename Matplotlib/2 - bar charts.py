from matplotlib import pyplot as plt
import numpy as np

# .style.use('theme name') puts a theme on the graph. Common ones are seaborn, fivethirtyeight...
plt.style.use("fivethirtyeight")

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# uses numpy to create an array with a range of the length of x
# doing this because using ages_x for all x coordinates for each .bar will cause them to stack on top of each other
x_indexes = np.arange(len(ages_x))

width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# use .bar(x,y) to create a bar graph
# width = a width to specify a fixed value for width of each bar
# color = color, label = label
plt.bar(x_indexes - width, dev_y, width = width, color="#444444", label="All Devs")

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes, py_dev_y, width = width, color="#008fd5", label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes + width, js_dev_y, width = width, color="#e5ae38", label="JavaScript")

plt.legend()

# changes the ticks of the x axis, then changes the labels to the values of ages
plt.xticks(ticks = x_indexes, labels = ages_x)

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.tight_layout()

plt.show()
