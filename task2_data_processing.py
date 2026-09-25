import pandas as pd

# Load collected data
df = pd.read_csv("trending_data.csv")

print("Original data:")
print(df.head())

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Remove duplicates
df = df.drop_duplicates()

# Replace missing values
df = df.fillna(0)

# Sort by date
df = df.sort_values("date")

# Save cleaned data
df.to_csv("cleaned_trending_data.csv", index=False)

print("\nData processing completed!")
print(df.head())