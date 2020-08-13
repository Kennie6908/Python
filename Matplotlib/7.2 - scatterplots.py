import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('matplotlib7.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

# to view scatterplot of view_count to likes on Youtube Video
# uses ratio value to determine color shade. Higher view to like ratio will be darker color.
plt.scatter(view_count, likes, c = ratio, cmap = 'summer', edgecolor = 'black', linewidth = 1, alpha = 0.75)

# create color bar legend.
cbar = plt.colorbar()
cbar.set_label('Like to Dislike Ratio')

# uses .xscale and .yscale to set the axis scale to log (10^x).
# this formats data to get rid of one really large outlier.
plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()
