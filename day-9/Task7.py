import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np
from scipy.stats import norm

iris = load_iris()
sepal_widths = iris.data[:, 1]

mean_sepal_width = np.mean(sepal_widths)
std_dev_sepal_width = np.std(sepal_widths)
sepal_width_rv = norm(loc=mean_sepal_width, scale=std_dev_sepal_width)
sepal_width_values = np.linspace(min(sepal_widths), max(sepal_widths), 100)
pdf_values = sepal_width_rv.pdf(sepal_width_values)

plt.figure(figsize=(8, 6))
plt.plot(sepal_width_values, pdf_values)
plt.xlabel('Sepal Width')
plt.ylabel('Probability Density')
plt.title('Probability Density Function of Sepal Widths')
plt.show()
