import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Global style
sns.set_style("darkgrid")

# Better figure quality
plt.rcParams['figure.figsize'] = (10,6)

# Bigger fonts
plt.rcParams['font.size'] = 12

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
colors = ['#E50914', '#221F1F']

plt.figure(figsize=(7,7))

plt.pie(
    type_counts,
    labels=type_counts.index,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    shadow=True,
    explode=[0.05, 0]
)

plt.title(
    "Netflix Content Distribution",
    fontsize=16,
    fontweight='bold'
)

plt.savefig("visualization_generated/content_distribution.png")

plt.show()

# Top 10 Ratings
ratings = df['rating'].value_counts().head(10)

plt.figure(figsize=(10,6))

sns.barplot(
    x=ratings.index,
    y=ratings.values,
    palette='rocket'
)

plt.title(
    "Top 10 Netflix Ratings",
    fontsize=16,
    fontweight='bold'
)

plt.xlabel("Rating")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visualization_generated/ratings_chart.png")

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

plt.savefig("visualization_generated/country_chart.png")

plt.show()

# movie duration distribution
movie_df = df[df['type'] == 'Movie'].copy()

movie_df['duration_int'] = movie_df['duration'].str.replace(' min', '').astype(float)

plt.figure(figsize=(10,5))

movie_df['duration_int'].hist(bins=30)

plt.title("Movie Duration Distribution")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")

plt.savefig("visualization_generated/movie_duration_chart.png")
plt.show()

#Movies Added Per Year
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df['year_added'] = df['date_added'].dt.year

yearly_additions = df['year_added'].value_counts().sort_index()

plt.figure(figsize=(12,5))

yearly_additions.plot(kind='line', marker='o')

plt.title("Content Added to Netflix Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")

plt.savefig("visualization_generated/yearly_additions_chart.png")
plt.show()

#Release Year Analysis
plt.figure(figsize=(10,5))

df['release_year'].hist(bins=10)

plt.title("Netflix Content Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")

plt.savefig("visualization_generated/release_year_chart.png")
plt.show()

# Remove missing listed_in values
genre_df = df.dropna(subset=['listed_in']).copy()

# Split genres
genre_df['listed_in'] = genre_df['listed_in'].str.split(',')

# Explode genres into separate rows
genre_exploded = genre_df.explode('listed_in')

# Remove extra spaces
genre_exploded['listed_in'] = genre_exploded['listed_in'].str.strip()

# Top 10 genres
top_genres = genre_exploded['listed_in'].value_counts().head(10)

# Plot
plt.figure(figsize=(12,6))

top_genres.sort_values().plot(kind='barh')

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.tight_layout()

plt.savefig("visualization_generated/top_genres_chart.png")

plt.show()

# Create numeric features
movie_df = df[df['type'] == 'Movie'].copy()

movie_df = movie_df.dropna(subset=['release_year'])

# Extract duration
movie_df['duration_int'] = movie_df['duration'].str.replace(
    ' min',
    '',
    regex=False
)

movie_df['duration_int'] = pd.to_numeric(
    movie_df['duration_int'],
    errors='coerce'
)

# Correlation matrix
corr = movie_df[['release_year', 'duration_int']].corr()

# Plot heatmap
plt.figure(figsize=(6,4))

sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("visualization_generated/correlation_heatmap.png")

plt.show()