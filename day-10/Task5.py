import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(X_test[:, 5], y_test, label='Actual')
plt.plot(X_test[:, 5], y_pred, color='red', label='Predicted')
plt.xlabel('Number of Rooms')
plt.ylabel('Target Variable')
plt.title('Linear Regression Model Performance')
plt.legend()
plt.show()
