import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv('titanic.csv')

plt.scatter(titanic['Age'], titanic['Fare'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Relationship between Age and Fare on the Titanic')
plt.show()
