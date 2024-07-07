import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv('titanic.csv')

sns.boxplot(x='Pclass', y='Fare', data=titanic, palette='viridis')
plt.title('Distribution of Fares by Passenger Class on the Titanic')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.show()

