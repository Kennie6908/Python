# what graph should I use?

# for trend --> sns.lineplot()


# for relationship:

# use sns.barplot() when comparing quantities corresponding to different groups.

# use sns.heatmap() to find color-coded patterns in tables of numbers.

# use sns.scatterplot() to show relationship between two continuous variables.
# if color coded, can also show relationship with a third categorical variable.

# use sns.regplot() to include a regression line in the scatterplot.

# use sns.lmplot() to draw multiple regression lines.
# useful if scatterplot contains multiple color coded groups.

# use sns.swarmplot() to show relationship between a continuous and a categorical variable.


# for distribution:

# use sns.displot() to show distribution of a single numerical variable.

# use sns.kdeplot() to show an estimated, smooth distribution of a single numerical variable.

# use sns.joinplot() to display a 2D KDE plot with the corresponding KDE plots of each individual variable.



# seaborn styles
# change using sns.set_style('style')
# 5 different styles. 'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'.
