import numpy as np
from matplotlib import pyplot as plt
import csv
from collections import Counter
import pandas as pd

plt.style.use('fivethirtyeight')

# import data from csv
data = pd.read_csv('matplotlib2-2.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']
language_counter = Counter()

# lang_responses is a list with languages and a delimeter ';'
# to get each language and update counter, use .update() on each item then .split('delimeter')
for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

# counter.most_common(number of most common)
# counter will have item tuple --> (language, count)
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

print(languages)
print(popularity)

# reversing it to get greatest to smallest on graph. To do the opposite, don't reverse the arrays.
languages.reverse()
popularity.reverse()

# to plot, use .barh(column, value)
plt.barh(languages, popularity)
plt.title("Most Popular Languages")
plt.xlabel("Number of People Who Use")
plt.tight_layout()

plt.show()
