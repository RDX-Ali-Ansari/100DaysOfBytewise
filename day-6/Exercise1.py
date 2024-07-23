from sklearn.datasets import load_iris
from sklearn.utils import Bunch

iris = load_iris()
X = iris.data
y = iris.target

print("First 5 rows of the Iris dataset:")
print(X[:5])
