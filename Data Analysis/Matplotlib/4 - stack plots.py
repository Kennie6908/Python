from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# x values
minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# y values
player1 = [0, 2, 1, 4, 2, 3, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#e5ae37', '#fc4f30']

# stackplot used to show cumulative result as well as individual values
# to plot, use .stackplot(x values, y values...)
# many arguments, important one is colors = colors. 
plt.stackplot(minutes, player1, player2, player3, labels = labels, colors = colors)

# move the legend using loc argument. Bottom left = (0,0)
plt.legend(loc = (0.07, 0.05))

plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()
