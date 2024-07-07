import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv('titanic.csv')

corr_matrix = titanic.corr()

sns.heatmap(corr_matrix, annot=True, cmap='YlOrRd')
plt.title('Correlation Matrix of the Titanic Dataset')
plt.show()
