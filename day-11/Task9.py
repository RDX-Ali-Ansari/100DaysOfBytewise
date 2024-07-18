import pandas as pd
from imblearn.over_sampling import SMOTE, ADASYN
from imblearn.under_sampling import RandomUnderSampler

# Load the dataset
credit_df = pd.read_csv('credit_card_fraud.csv')

# Separate features and target
X = credit_df.drop('Class', axis=1)
y = credit_df['Class']

# SMOTE
smote = SMOTE()
X_smote, y_smote = smote.fit_resample(X, y)

# ADASYN
adasyn = ADASYN()
X_adasyn, y_adasyn = adasyn.fit_resample(X, y)

# Undersampling
undersampler = RandomUnderSampler()
X_undersampled, y_undersampled = undersampler.fit_resample(X, y)

print("Original dataset shape:", y.value_counts())
print("SMOTE dataset shape:", pd.Series(y_smote).value_counts())
print("ADASYN dataset shape:", pd.Series(y_adasyn).value_counts())
print("Undersampled dataset shape:", pd.Series(y_undersampled).value_counts())
