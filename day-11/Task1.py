import pandas as pd
from sklearn.impute import SimpleImputer

# Load the dataset
titanic_df = pd.read_csv('titanic.csv')

# Display missing values
print(titanic_df.isnull().sum())

# Mean/Median Imputation
imputer_mean = SimpleImputer(strategy='mean')
titanic_df['Age'] = imputer_mean.fit_transform(titanic_df[['Age']])

# Mode Imputation
imputer_mode = SimpleImputer(strategy='most_frequent')
titanic_df['Embarked'] = imputer_mode.fit_transform(titanic_df[['Embarked']])

# Dropping rows/columns with missing values
titanic_df_dropped_rows = titanic_df.dropna()
titanic_df_dropped_columns = titanic_df.dropna(axis=1)

# Display the dataset after handling missing values
print(titanic_df.isnull().sum())
