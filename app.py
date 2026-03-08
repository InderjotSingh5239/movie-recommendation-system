import streamlit as st
from model import recommend

genres = ["Action","Comedy","Sci-Fi","Romance","Thriller","Horror"]

st.title("Movie Recommendation System")

genre = st.selectbox("Choose a Genre", genres)

if st.button("Recommend"):
    results = recommend(genre)

    for movie in results:
        st.write(movie)

