import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD THE DATA
# Pandas automatically handles .gz compression. 
# If you used a .zip file, use: pd.read_csv('ratings.csv.zip', compression='zip')
try:
    ratings = pd.read_csv('ratings.csv') 
    movies = pd.read_csv('movies.csv')
    print("✅ Files loaded successfully!")
except FileNotFoundError:
    print("❌ Error: Ensure 'ratings.csv.gz' and 'movies.csv' are in the same folder.")

# 2. MERGE DATASETS
# We combine them on 'movieId' so we have titles and ratings in one table
df = pd.merge(ratings, movies, on='movieId')

# 3. DATA CLEANING & PREPARATION
# Convert timestamp to a readable date format (optional but good for analysis)
df['date'] = pd.to_datetime(df['timestamp'], unit='s')

# 4. BASIC STATISTICS
print("\n--- Project Statistics ---")
print(f"Total Ratings: {len(df)}")
print(f"Unique Movies: {df['title'].nunique()}")
print(f"Average Movie Rating: {df['rating'].mean():.2f}")

# 5. FIND TOP 10 HIGHEST RATED MOVIES
# We filter for movies with more than 100 ratings to keep it accurate
movie_stats = df.groupby('title')['rating'].agg(['mean', 'count'])
top_rated = movie_stats[movie_stats['count'] > 100].sort_values(by='mean', ascending=False).head(10)

print("\n--- Top 10 Recommended Movies (Min. 100 ratings) ---")
print(top_rated)

# 6. VISUALIZATION 1: Distribution of Ratings
plt.figure(figsize=(10, 5))
sns.countplot(x='rating', data=df, palette='viridis')
plt.title('Distribution of Movie Ratings', fontsize=15)
plt.xlabel('Rating Score')
plt.ylabel('Number of Users')
plt.savefig('rating_distribution.png') # Saves for your GitHub repo
print("\n✅ Visualization 1 saved: rating_distribution.png")

# 7. VISUALIZATION 2: Top Genres by Popularity
# We split the genres string (e.g., "Adventure|Children|Fantasy")
genres = df['genres'].str.split('|', expand=True).stack().value_counts()

plt.figure(figsize=(12, 6))
genres.head(10).plot(kind='bar', color='salmon')
plt.title('Top 10 Most Rated Genres', fontsize=15)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_genres.png')
print("✅ Visualization 2 saved: top_genres.png")

print("\n🚀 Execution Complete! Check your folder for the .png report files.")
