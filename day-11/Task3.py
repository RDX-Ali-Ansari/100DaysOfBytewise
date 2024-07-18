import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt

# Load the dataset
wine_df = pd.read_csv('wine_quality.csv')

# Standardization
scaler_standard = StandardScaler()
wine_df_standardized = pd.DataFrame(scaler_standard.fit_transform(wine_df), columns=wine_df.columns)

# Normalization
scaler_minmax = MinMaxScaler()
wine_df_normalized = pd.DataFrame(scaler_minmax.fit_transform(wine_df), columns=wine_df.columns)

# Plotting the distributions before and after scaling
fig, axes = plt.subplots(3, 1, figsize=(12, 18))
wine_df.hist(ax=axes[0])
wine_df_standardized.hist(ax=axes[1])
wine_df_normalized.hist(ax=axes[2])
plt.show()
