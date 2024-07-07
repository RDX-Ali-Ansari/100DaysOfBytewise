from sklearn.datasets import load_iris
import numpy as np
from scipy.stats import norm

iris = load_iris()
petal_lengths = iris.data[:, 2]

mean_petal_length = np.mean(petal_lengths)
std_dev_petal_length = np.std(petal_lengths)
petal_length_rv = norm(loc=mean_petal_length, scale=std_dev_petal_length)

given_petal_length = 5.0
probability = 1 - petal_length_rv.cdf(given_petal_length)

print(f"Probability of petal length greater than {given_petal_length} cm: {probability:.4f}")
