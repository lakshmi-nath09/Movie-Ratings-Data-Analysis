import pandas as pd

# Load the data
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv') 

# Merge and print the results
df = pd.merge(ratings, movies, on='movieId')
print("--- SUCCESS: DATA LOADED ---")
print(df.head())
