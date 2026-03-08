import pandas as pd

# load dataset
movies = pd.read_csv("movies.csv")

# fill empty values
movies = movies.fillna('')

def recommend(selected_genre):

    # filter movies by genre
    filtered_movies = movies[movies["genre"] == selected_genre]

    # take first 5 movies
    recommended_movies = filtered_movies["title"].head(5).tolist()

    return recommended_movies
