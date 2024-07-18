import pandas as pd

# Load the datasets
ratings = pd.read_csv('ratings.csv')
users = pd.read_csv('users.csv')
movies = pd.read_csv('movies.csv')

# Merging datasets
merged_df = ratings.merge(users, on='user_id').merge(movies, on='movie_id')

print(merged_df.head())
