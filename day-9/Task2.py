from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
petal_widths = iris.data[:, 3]

variance_petal_width = np.var(petal_widths)
std_dev_petal_width = np.sqrt(variance_petal_width)

print(f"Variance of petal width: {variance_petal_width:.2f}")
print(f"Standard deviation of petal width: {std_dev_petal_width:.2f}")
