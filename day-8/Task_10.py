import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

titanic = pd.read_csv('titanic.csv')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(titanic['Age'], bins=20, edgecolor='black')
ax1.set_title('Age Distribution')
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency')

sns.kdeplot(titanic['Age'], shade=True, ax=ax2)
ax2.set_title('Age Distribution (KDE)')
ax2.set_xlabel('Age')
ax2.set_ylabel('Density')

plt.tight_layout()
plt.show()
