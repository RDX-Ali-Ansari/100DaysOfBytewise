import matplotlib.pyplot as plt

plt.hist(X[:, 0], bins=20)
plt.xlabel("Feature 1")
plt.ylabel("Frequency")
plt.title("Distribution of Feature 1")
plt.show()
