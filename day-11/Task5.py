import pandas as pd
from sklearn.impute import KNNImputer
from fancyimpute import IterativeImputer

# Load the dataset
retail_df = pd.read_csv('retail_sales.csv')

# KNN Imputation
knn_imputer = KNNImputer(n_neighbors=5)
retail_df_knn_imputed = pd.DataFrame(knn_imputer.fit_transform(retail_df), columns=retail_df.columns)

# MICE Imputation
mice_imputer = IterativeImputer()
retail_df_mice_imputed = pd.DataFrame(mice_imputer.fit_transform(retail_df), columns=retail_df.columns)

print(retail_df_knn_imputed.head())
print(retail_df_mice_imputed.head())
