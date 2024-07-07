from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
sepal_lengths = iris.data[:, 0]
sepal_widths = iris.data[:, 1]

covariance = np.cov(sepal_lengths, sepal_widths)[0, 1]
correlation = np.corrcoef(sepal_lengths, sepal_widths)[0, 1]

print(f"Covariance between sepal length and sepal width: {covariance:.2f}")
print(f"Correlation between sepal length and sepal width: {correlation:.2f}")

if correlation > 0:
    print("There is a positive correlation between sepal length and sepal width.")
elif correlation < 0:
    print("There is a negative correlation between sepal length and sepal width.")
else:
    print("There is no correlation between sepal length and sepal width.")
