from sklearn.datasets import load_iris
import numpy as np
from scipy.stats import norm

iris = load_iris()
sepal_lengths = iris.data[:, 0]

mean_sepal_length = np.mean(sepal_lengths)
std_dev_sepal_length = np.std(sepal_lengths)
sepal_length_rv = norm(loc=mean_sepal_length, scale=std_dev_sepal_length)

sepal_length_values = np.linspace(min(sepal_lengths), max(sepal_lengths), 100)
probabilities = sepal_length_rv.pdf(sepal_length_values)

print("Probability distribution of sepal lengths:")
for length, prob in zip(sepal_length_values, probabilities):
    print(f"Sepal length: {length:.2f}, Probability: {prob:.4f}")
