import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv('titanic.csv')

list = titanic['Age'].value_counts().sort_index()

plt.plot(list)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Trend of Age on the Titanic')
plt.show()
