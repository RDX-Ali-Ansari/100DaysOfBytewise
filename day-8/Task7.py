import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv('titanic.csv')

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].hist(titanic['Age'], bins=20)
axes[0, 0].set_title('Age Distribution')
axes[0, 0].set_xlabel('Age')
axes[0, 0].set_ylabel('Frequency')

axes[0, 1].scatter(titanic['Age'], titanic['Fare'])
axes[0, 1].set_title('Age vs Fare')
axes[0, 1].set_xlabel('Age')
axes[0, 1].set_ylabel('Fare')

titanic['Pclass'].value_counts().plot(kind='bar', ax=axes[1, 0])
axes[1, 0].set_title('Passenger Class Distribution')
axes[1, 0].set_xlabel('Passenger Class')
axes[1, 0].set_ylabel('Count')

sns.boxplot(x='Pclass', y='Fare', data=titanic, ax=axes[1, 1])
axes[1, 1].set_title('Fare Distribution by Passenger Class')
axes[1, 1].set_xlabel('Passenger Class')
axes[1, 1].set_ylabel('Fare')

plt.tight_layout()
plt.show()
