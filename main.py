import pandas as pd

# Load the data
movies = pd.read_csv('movie.csv')
ratings = pd.read_csv('ratings.csv') 

# Merge and print the results
df = pd.merge(ratings, movie, on='movieId')
print("--- SUCCESS: DATA LOADED ---")
print(df.head())
