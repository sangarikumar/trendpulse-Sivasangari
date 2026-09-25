import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_trending_data.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Create graph
plt.figure(figsize=(12, 6))

plt.plot(
    df["date"],
    df["Python"],
    label="Python"
)

plt.plot(
    df["date"],
    df["Artificial Intelligence"],
    label="Artificial Intelligence"
)

plt.plot(
    df["date"],
    df["Data Science"],
    label="Data Science"
)

plt.plot(
    df["date"],
    df["Machine Learning"],
    label="Machine Learning"
)

plt.title("Technology Trends")
plt.xlabel("Date")
plt.ylabel("Search Interest")

plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()

# Save graph
plt.savefig("trend_analysis.png")

# Display graph
plt.show()

print("Visualization completed!")