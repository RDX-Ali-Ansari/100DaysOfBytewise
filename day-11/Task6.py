import pandas as pd

# Load the dataset
heart_df = pd.read_csv('heart_disease.csv')

# Creating age groups
heart_df['AgeGroup'] = pd.cut(heart_df['age'], bins=[0, 30, 50, 80], labels=['Young', 'Middle-aged', 'Old'])

# Creating cholesterol level categories
heart_df['CholesterolLevel'] = pd.cut(heart_df['cholesterol'], bins=[0, 200, 240, 600], labels=['Normal', 'Borderline High', 'High'])

print(heart_df[['age', 'AgeGroup', 'cholesterol', 'CholesterolLevel']].head())
