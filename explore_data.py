import pandas as pd

df = pd.read_csv("goa_temperature_clean.csv")
df["time"] = pd.to_datetime(df["time"])

print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nBasic stats:")
print(df["temperature"].describe())

print("\nAny missing values?", df["temperature"].isna().sum())