import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset
titanic = pd.read_csv('titanic.csv')

# Extract the 'Survived' column and convert it to a list of values
survived_counts = titanic['Survived'].value_counts().sort_index()

# Create a line plot
plt.figure(figsize=(8, 6))
plt.plot(survived_counts)
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.title('Trend of Survival on the Titanic')
plt.show()
