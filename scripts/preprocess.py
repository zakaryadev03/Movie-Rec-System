import pandas as pd

ratings = pd.read_csv('../data/raw/ratings.csv')
movies = pd.read_csv('../data/raw/movies.csv')

# Remove duplicates
ratings = ratings.drop_duplicates(subset=['userId', 'movieId'], keep='last')
print("Shape after deduplication:", ratings.shape)

# Remove rare movies
movie_rating_counts = ratings['movieId'].value_counts()
valid_movies = movie_rating_counts[movie_rating_counts > 5].index
ratings = ratings[ratings['movieId'].isin(valid_movies)]
print("Shape after filtering rare movies:", ratings.shape)

# Remove inactive users
user_rating_counts = ratings['userId'].value_counts()
valid_users = user_rating_counts[user_rating_counts > 2].index
ratings = ratings[ratings['userId'].isin(valid_users)]
print("Shape after filtering inactive users:", ratings.shape)

# drop the timestamp column (not needed)
ratings = ratings.drop(columns=['timestamp'])

# Align movies with ratings
movies = movies[movies['movieId'].isin(ratings['movieId'].unique())]
print("Movies shape after alignment:", movies.shape)

# Save cleaned data
ratings.to_csv('../data/cleaned/cleaned_ratings.csv', index=False)
movies.to_csv('../data/cleaned/cleaned_movies.csv', index=False)