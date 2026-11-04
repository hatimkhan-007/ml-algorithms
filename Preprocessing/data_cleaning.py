import pandas as pd
from sklearn.model_selection import Min_Max_

df = pd.read_csv("../Dataset/customer_churn_dataset.csv")

missing_before = df["age"].isna().sum()
print(f"Missing values before imputation: {missing_before}")

df["age"] = df["age"].fillna(df["age"].mean())

missing_after = df["age"].isna().sum()
print(f"Missing values after imputation: {missing_after}")
