import pandas as pd

# Load the data
movies = pd.read_csv('movie.csv')

# Add compression='gzip' so Python knows how to unzip it
ratings = pd.read_csv('ratings.csv', compression='gzip') 

# Merge and print the results
df = pd.merge(ratings, movies, on='movieId')
print("--- SUCCESS: DATA LOADED ---")
print(df.head())
