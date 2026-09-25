from pytrends.request import TrendReq

# Connect to Google Trends
pytrends = TrendReq(hl="en-US", tz=360)

# Topics to track
keywords = [
    "Python",
    "Artificial Intelligence",
    "Data Science",
    "Machine Learning"
]

# Get data for the last 7 days in India
pytrends.build_payload(
    keywords,
    timeframe="now 7-d",
    geo="IN"
)

# Collect trend data
data = pytrends.interest_over_time()

# Remove unnecessary column
if "isPartial" in data.columns:
    data = data.drop(columns=["isPartial"])

# Save data
data.to_csv("trending_data.csv")

print("Data collection completed!")
print(data.head())