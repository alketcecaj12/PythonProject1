# The WorldCups dataset that I found on Kaggle contains data about all the FIFA World Cups since 1930
# The analysis shows a sorted list of the countries that won the WorldCup the most
# It also shows a list of countries sorted by which country was a runner-up the most and finally,
# how many times the FIFA WorlCup was hosted by a certain country
# The last piece of code shows the scatterplot between the 'Year of World Cup' and the 'Number od matches played'. As the
# number of participants increases also increases the number of matches played per FIFA World Cup.

# Import pandas
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

# Read the file into a DataFrame: df
df = pd.read_csv('WorldCups.csv')


print('----------- Times Winner of FIFA World Cup --------------')
print(df['Winner'].value_counts(dropna=False))


print('----------- Times Runners-Up Country of FIFA World Cup -------------')
print(df['Runners-Up'].value_counts(dropna=False))


print('----------- Times Hosting Country of FIFA World Cup --------------')
print(df['Country'].value_counts(dropna=False))

numpy_matrix = df.as_matrix()

print('-- years')
years = np.array(numpy_matrix[:,0])
print(years)

attend = np.array(numpy_matrix[:,8])
print('--- attend')
print(attend)

plt.scatter(years, attend, alpha=0.5)
plt.xlabel('Years')
plt.ylabel('Number of matches played')
plt.title('Scatter plot of \'Years\' vs \'Nr. of matches played\' per World Cup.')
plt.show()