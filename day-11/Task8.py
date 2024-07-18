import pandas as pd
from sklearn.feature_selection import mutual_info_classif, RFE
from sklearn.linear_model import LogisticRegression
import seaborn as sns

# Load the dataset
diabetes_df = pd.read_csv('diabetes.csv')

# Correlation Analysis
correlation_matrix = diabetes_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# Mutual Information
X = diabetes_df.drop('Outcome', axis=1)
y = diabetes_df['Outcome']
mutual_info = mutual_info_classif(X, y)
mutual_info_series = pd.Series(mutual_info, index=X.columns)
mutual_info_series.sort_values(ascending=False).plot(kind='bar')
plt.show()

# Recursive Feature Elimination (RFE)
model = LogisticRegression(max_iter=200)
rfe = RFE(model, n_features_to_select=5)
rfe.fit(X, y)
selected_features = X.columns[rfe.support_]
print("Selected Features by RFE:", selected_features)
