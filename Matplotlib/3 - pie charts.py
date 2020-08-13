from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# value of slices
slices = [59219, 55466, 47544, 36443, 35917]

# labels in corresponding order with slice values
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

# explode means to emphasize a slice by popping it out
explode = [0, 0, 0, 0.3, 0]

# to plot a pie graph, use .pie(slices)
# arguments include labels, explode, shadow, startangle, autopct (to get percentage label inside slice)
# also have wedgeprops to change each wedge/slice. ex. edgecolor, linewidth...
plt.pie(slices, labels = labels, wedgeprops = {'edgecolor': 'black'}, explode = explode,
            shadow = True, startangle = 90, autopct = '%.1f%%')

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()
