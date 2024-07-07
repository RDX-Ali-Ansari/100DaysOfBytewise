from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import numpy as np

boston = load_boston()
X = boston.data
y = boston.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
