import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing country values
df['country'] = df['country'].fillna('Unknown')

# Count Movies vs TV Shows
type_counts = df['type'].value_counts()

print("\nMovies vs TV Shows:")
print(type_counts)

# Plot Pie Chart
plt.figure(figsize=(6,6))
plt.pie(
    type_counts,
    labels=type_counts.index,
    autopct='%1.1f%%'
)

plt.title("Netflix Content Distribution")
plt.savefig("screenshots/content_distribution.png")
plt.show()

# Top 10 Ratings
ratings = df['rating'].value_counts().head(10)

plt.figure(figsize=(8,5))
ratings.plot(kind='bar')

plt.title("Top 10 Netflix Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.savefig("screenshots/ratings_chart.png")
plt.show()

# Top 10 Countries
countries = df['country'].value_counts().head(10)

plt.figure(figsize=(10,5))
countries.plot(kind='bar')

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.savefig("screenshots/country_chart.png")
plt.show()

print("\nAnalysis Completed Successfully!")