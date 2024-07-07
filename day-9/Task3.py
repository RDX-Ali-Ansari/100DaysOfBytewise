from sklearn.datasets import load_iris
import numpy as np
import pandas as pd

iris = load_iris()
feature_names = iris.feature_names
X = iris.data

summary_stats = pd.DataFrame({
    'Feature': feature_names,
    'Mean': np.mean(X, axis=0),
    'Median': np.median(X, axis=0),
    'Variance': np.var(X, axis=0),
    'Standard Deviation': np.std(X, axis=0)
})

print(summary_stats)
