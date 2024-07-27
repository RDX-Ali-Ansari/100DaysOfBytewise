
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, confusion_matrix

loan_data = pd.read_csv('loan_data.csv')

loan_data['gender'] = loan_data['gender'].fillna(loan_data['gender'].mode()[0])
loan_data['married'] = loan_data['married'].fillna(loan_data['married'].mode()[0])

cat_features = ['gender', 'married', 'education', 'self_employed', 'property_area']
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), cat_features)
    ])
X = preprocessor.fit_transform(loan_data)
y = loan_data['loan_status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print("\nConfusion Matrix:\n", conf_matrix)
