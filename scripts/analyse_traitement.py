import pandas as pd

# Load the cleaned data
df = pd.read_csv("../data/cleaned/cleaned_ratings.csv")

# Load movie titles (if available)
try:
    movies = pd.read_csv("../data/cleaned/cleaned_movies.csv")  # Adjust path if needed
    df = df.merge(movies, on="movieId", how="left")
except FileNotFoundError:
    print("Movie titles file not found. Skipping movie title analysis.")

# Compute average rating per movie
if 'title' in df.columns:
    movie_ratings = df.groupby("title")["rating"].mean().reset_index()
    
    # Top 10 best-rated movies
    top_movies = movie_ratings.sort_values(by="rating", ascending=False).head(10)
    print("\nTop 10 Movies:\n", top_movies)
    
    # Worst 10 movies
    worst_movies = movie_ratings.sort_values(by="rating", ascending=True).head(10)
    print("\nWorst 10 Movies:\n", worst_movies)

    # Most popular movies (highest number of ratings)
    popular_movies = df.groupby("title").size().reset_index(name="num_ratings")
    top_rated_movies = popular_movies.sort_values(by="num_ratings", ascending=False).head(10)
    print("\nMost Popular Movies:\n", top_rated_movies)
