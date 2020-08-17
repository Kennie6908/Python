import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

# corresponding x and y values
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

# can specify shades of colors for each corresponding x and y. Larger number means darker shade of color.
colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]

# can also specify size of each point. A larger number means a larger marker at that point.
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174, 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

# to create scatterplot, use .scatter(x, y)
# some arguments are single letters.
# s = sizes. c = colors. cmap = 'a color theme, which can be looked up'
# other arguments are marker, edgecolor, linewidth, alpha...
plt.scatter(x,y, s = sizes, c = colors, cmap = 'Greens', marker = 'X', edgecolor = 'black', linewidth = 1, alpha = 0.75)

# to create a colored bar that acts as a legend if you are doing colors
# use .colorbar()
# then call .set_label('label name')
cbar = plt.colorbar()
cbar.set_label('Satisfaction')

plt.tight_layout()

plt.show()
