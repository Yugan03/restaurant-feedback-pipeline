import pandas as pd

df = pd.read_csv("data/raw/Restaurant_Reviews.csv")

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head(5))
print(df["Rating"].value_counts(dropna=False).head())