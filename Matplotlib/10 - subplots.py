import pandas as pd
from matplotlib import pyplot as plt

# use subplots to have more control over the number of figures, axes, title and labels

plt.style.use('seaborn')

data = pd.read_csv('matplotlib10.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# assigns 1 figure, and two subplots (ax1 and ax2)
# ax1 and ax2 are deconstructed, so each of them will be one subplot with these parameters.
# use .subplots(nrows = 'number', ncols = 'number') to create subplot shape. This one will have two subplots, one on top of each other.
# can use sharex and sharey = True to have each subplot share an axis label.
fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, sharex = True)

# replace plt.plot with the subplot object that we are working with
# this will create first subplot with dev_salaries.
ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

# this will create second subplot with the rest of the salaries.
ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

# can control what each subplot has.
# CAREFUL, .title() --> .set_title and .xlabel()/.ylabel() --> .set_xlabel() and .set_ylabel()
ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

# can still use plt.tight_layout() and plt.show() since those apply to the entire plot, not any subplots. 
plt.tight_layout()

plt.show()
