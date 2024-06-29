import pandas as pd

df = pd.read_csv("data.csv")
print("Summary statistics for each column:")
print(df.describe())
