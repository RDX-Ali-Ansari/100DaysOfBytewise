import pandas as pd
import numpy as np
from scipy.stats import boxcox
import matplotlib.pyplot as plt

# Load the dataset
bike_df = pd.read_csv('bike_sharing.csv')

# Log Transformation
bike_df['log_count'] = np.log1p(bike_df['count'])

# Square Root Transformation
bike_df['sqrt_count'] = np.sqrt(bike_df['count'])

# Box-Cox Transformation
bike_df['boxcox_count'], _ = boxcox(bike_df['count'] + 1)  # Add 1 to avoid zero values

# Plotting the transformations
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
bike_df['count'].hist(ax=axes[0, 0], bins=30)
axes[0, 0].set_title('Original Count')
bike_df['log_count'].hist(ax=axes[0, 1], bins=30)
axes[0, 1].set_title('Log Transformed Count')
bike_df['sqrt_count'].hist(ax=axes[1, 0], bins=30)
axes[1, 0].set_title('Square Root Transformed Count')
bike_df['boxcox_count'].hist(ax=axes[1, 1], bins=30)
axes[1, 1].set_title('Box-Cox Transformed Count')
plt.show()
