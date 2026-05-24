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
# Remove rows where country is missing
country_df = df.dropna(subset=['country'])

# Remove rows where country is 'Unknown'
country_df = country_df[country_df['country'] != 'Unknown']

# Top 10 countries
countries = country_df['country'].value_counts().head(10)

plt.figure(figsize=(10,5))

countries.plot(kind='bar')

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.savefig("country_chart.png")

plt.show()

# movie duration distribution
movie_df = df[df['type'] == 'Movie'].copy()

movie_df['duration_int'] = movie_df['duration'].str.replace(' min', '').astype(float)

plt.figure(figsize=(10,5))

movie_df['duration_int'].hist(bins=30)

plt.title("Movie Duration Distribution")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")

plt.savefig("movie_duration_chart.png")
plt.show()