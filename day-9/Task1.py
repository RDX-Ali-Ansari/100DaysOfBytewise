from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
sepal_lengths = iris.data[:, 0]

mean_sepal_length = np.mean(sepal_lengths)
median_sepal_length = np.median(sepal_lengths)
mode_sepal_length = np.round(np.mean(sepal_lengths))

print(f"Mean sepal length: {mean_sepal_length:.2f}")
print(f"Median sepal length: {median_sepal_length:.2f}")
print(f"Mode sepal length: {mode_sepal_length:.2f}")
