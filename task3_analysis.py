import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_trending_data.csv")

topics = [
    "Python",
    "Artificial Intelligence",
    "Data Science",
    "Machine Learning"
]

# Calculate average interest
average_interest = df[topics].mean()

print("Average interest:")
print(average_interest)

# Find the topic with highest average interest
most_popular = average_interest.idxmax()

print("\nMost popular topic:")
print(most_popular)

# Calculate maximum interest
maximum_interest = df[topics].max()

print("\nMaximum interest:")
print(maximum_interest)

# Save results
results = pd.DataFrame({
    "Average Interest": average_interest,
    "Maximum Interest": maximum_interest
})

results.to_csv("analysis_results.csv")

print("\nAnalysis completed!")