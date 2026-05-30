import pandas as pd

df = pd.read_csv("goa_temperature.csv")
df["time"] = pd.to_datetime(df["time"])

print("Before cleaning:", df.shape)
print("Missing values:", df["temperature"].isna().sum())

# Drop rows with missing temperature
df = df.dropna(subset=["temperature"])

print("After dropping nulls:", df.shape)

# Check for duplicate timestamps
duplicates = df.duplicated(subset=["time"]).sum()
print("Duplicate timestamps:", duplicates)
df = df.drop_duplicates(subset=["time"])

# Make sure data is sorted by time
df = df.sort_values("time").reset_index(drop=True)

# Save cleaned version
df.to_csv("goa_temperature_clean.csv", index=False)

print("\nDate range:", df["time"].min(), "→", df["time"].max())
print("Total hours of clean data:", len(df))
print(df.tail())