import pandas as pd
import matplotlib.pyplot as plt

data = {'Categories': ['Category A', 'Category B', 'Category C', 'Category D'],
        'Sizes': [15, 30, 45, 10]}

df = pd.DataFrame(data)
df.set_index('Categories', inplace=True)

ax = df.plot.pie(y='Sizes', autopct='%1.1f%%', startangle=140, legend=False)
ax.set_ylabel('')
plt.title('My Pie Chart')
plt.show()