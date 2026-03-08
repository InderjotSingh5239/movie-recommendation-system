import streamlit as st
import pandas as pd
from model import recommend

movies = pd.read_csv("dataset/movies.csv")

st.title("Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.write("Recommended Movies:")

    for movie in recommendations:
        st.write(movie)