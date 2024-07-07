import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv('titanic.csv')

sns.violinplot(x='Pclass', y='Age', data=titanic)
plt.title('Age Distribution by Passenger Class on the Titanic')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.show()
