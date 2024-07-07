import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np
from scipy.stats import norm

iris = load_iris()
sepal_lengths = iris.data[:, 0]

mean_sepal_length = np.mean(sepal_lengths)
std_dev_sepal_length = np.std(sepal_lengths)
sepal_length_rv = norm(loc=mean_sepal_length, scale=std_dev_sepal_length)

plt.figure(figsize=(8, 6))
plt.hist(sepal_lengths, bins=20, density=True, edgecolor='black')
plt.plot(sepal_length_values, probabilities, color='red')
plt.xlabel('Sepal Length')
plt.ylabel('Probability Density')
plt.title('Probability Distribution of Sepal Lengths')
plt.show()
