import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load the dataset
boston_df = pd.read_csv('boston_housing.csv')

# Z-score
z_scores = np.abs(stats.zscore(boston_df))
boston_df_zscore = boston_df[(z_scores < 3).all(axis=1)]

# IQR
Q1 = boston_df.quantile(0.25)
Q3 = boston_df.quantile(0.75)
IQR = Q3 - Q1
boston_df_iqr = boston_df[~((boston_df < (Q1 - 1.5 * IQR)) | (boston_df > (Q3 + 1.5 * IQR))).any(axis=1)]

# Visualization
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Original Data')
boston_df.boxplot()
plt.subplot(1, 2, 2)
plt.title('Data After Removing Outliers')
boston_df_zscore.boxplot()
plt.show()
