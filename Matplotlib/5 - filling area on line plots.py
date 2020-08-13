import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('matplotlib5.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# creating two regular line graphs
plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

# use .fill_between to fill between a line and another value.
# .fill_between(x values, y values, another set of y values) to fill in between the two y values.
# can use where = (condition) argument to specify how to fill. Ex. color = 'something', alpha = 'something', label = 'something'
plt.fill_between(ages, py_salaries, dev_salaries,
                where= (py_salaries > dev_salaries), interpolate = True, alpha = 0.25, label = 'aboveavg')

plt.fill_between(ages, py_salaries, dev_salaries,
                where= (py_salaries < dev_salaries), interpolate = True, color = 'red', alpha = 0.5, label = 'belowavg')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
