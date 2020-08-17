import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('matplotlib10.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# this is creating two different figures (screens), and in each figure, there will be one subplot.
# Again, use subplots to have more control over all the elements in each figure. Just in case you want to add more than one graph.
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# plotting and labeling everything on the subplot in figure 1
ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

# be careful to use .set_title() and .set_x or y label() when working with subplots.
ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

# plotting and labeling everything on the subplot in figure 2
ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

# be careful to use .set_title() and .set_x or y label() when working with subplots. 
ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

# again, using plt.tight_layout() and plt.show() since those affect everything, not each figure or subplot.
plt.tight_layout()

plt.show()

# to save each figure, use nameoffig.savefig('filename')
fig1.savefig('fig1.png')
fig2.savefig('fig2.png')
