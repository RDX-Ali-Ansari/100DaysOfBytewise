import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the dataset
car_df = pd.read_csv('car_evaluation.csv')

# One-Hot Encoding
one_hot_encoder = OneHotEncoder(sparse=False)
car_df_one_hot = pd.DataFrame(one_hot_encoder.fit_transform(car_df))

# Label Encoding
label_encoder = LabelEncoder()
for column in car_df.columns:
    car_df[column] = label_encoder.fit_transform(car_df[column])

print(car_df_one_hot.head())
print(car_df.head())
