from sklearn.datasets import load_iris
import numpy as np
from scipy.stats import ttest_ind

iris = load_iris()
petal_lengths = iris.data[:, 2]
species = iris.target

setosa_petal_lengths = petal_lengths[species == 0]
versicolor_petal_lengths = petal_lengths[species == 1]

t_stat, p_value = ttest_ind(setosa_petal_lengths, versicolor_petal_lengths)

print(f"t-statistic: {t_stat:.2f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("There is a significant difference in the mean petal length between Setosa and Versicolor species.")
else:
    print("There is no significant difference in the mean petal length between Setosa and Versicolor species.")
