import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv('titanic.csv')
titanic['Pclass'].value_counts().plot(kind='bar')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.title('Frequency of Passenger Classes on the Titanic')
plt.show()
