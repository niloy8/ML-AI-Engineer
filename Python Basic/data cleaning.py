import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", None],
    "Age": [25, 30, None, 22, 28],
    "Salary": ["50000", "60000", "not available", "45000", "52000"],
    "Department": ["HR", "IT", "IT", None, "HR"]
}

df = pd.DataFrame(data)
# print(df)

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())


df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df.isnull().sum())