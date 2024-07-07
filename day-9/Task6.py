import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np
from scipy.stats import norm

iris = load_iris()
petal_lengths = iris.data[:, 2]

mean_petal_length = np.mean(petal_lengths)
std_dev_petal_length = np.std(petal_lengths)
petal_length_rv = norm(loc=mean_petal_length, scale=std_dev_petal_length)
petal_length_values = np.linspace(min(petal_lengths), max(petal_lengths), 100)
cdf_values = petal_length_rv.cdf(petal_length_values)

plt.figure(figsize=(8, 6))
plt.plot(petal_length_values, cdf_values)
plt.xlabel('Petal Length')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Function of Petal Lengths')
plt.show()
