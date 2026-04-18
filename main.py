import pandas as pd

# 1. Load your Movies file (Capital M as per your GitHub)
movies = pd.read_csv('movie.csv')

# 2. Load the small sample we just made (No compression errors!)
ratings = pd.read_csv('ratings_sample.csv') 

# 3. Merge them using the movieId column
df = pd.merge(ratings, movies, on='movieId')

# 4. Print the result
print("--- SUCCESS: PROJECT EXECUTED ---")
print(df[['title', 'rating']])
