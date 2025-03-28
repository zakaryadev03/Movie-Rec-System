import pandas as pd

ratings = pd.read_csv('data/raw/ratings.csv')
movies = pd.read_csv('data/raw/movies.csv')

ratings = ratings.drop_duplicates(subset=['userId', 'movieId'], keep='last')
print("Shape after deduplication:", ratings.shape)

movie_rating_counts = ratings['movieId'].value_counts()
valid_movies = movie_rating_counts[movie_rating_counts > 5].index
ratings = ratings[ratings['movieId'].isin(valid_movies)]
print("Shape after filtering rare movies:", ratings.shape)

user_rating_counts = ratings['userId'].value_counts()
valid_users = user_rating_counts[user_rating_counts > 2].index
ratings = ratings[ratings['userId'].isin(valid_users)]
print("Shape after filtering inactive users:", ratings.shape)

ratings = ratings.drop(columns=['timestamp'])

movies = movies[movies['movieId'].isin(ratings['movieId'].unique())]
print("Movies shape after alignment:", movies.shape)

ratings.to_csv('data/cleaned/cleaned_ratings.csv', index=False)
movies.to_csv('data/cleaned/cleaned_movies.csv', index=False)