import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.boxplot(x='Pclass', y='Fare', data=titanic)
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.title('Distribution of Fares by Passenger Class on the Titanic')
plt.show()
