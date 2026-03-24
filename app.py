import streamlit as st
import pandas as pd
from model import recommend

# Page config
st.set_page_config(page_title="Movie Recommender", layout="centered")

# Title
st.title("🎬 Movie Recommendation System")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("movies.csv")

movies = load_data()

# Get unique genres automatically
genres = movies["genre"].dropna().unique()

# Dropdown for genre selection
selected_genre = st.selectbox("Select a Genre", genres)

# Button
if st.button("Recommend Movies"):

    recommendations = recommend(selected_genre)

    if len(recommendations) == 0:
        st.warning("No movies found for this genre.")
    else:
        st.subheader("Recommended Movies:")
        
        for movie in recommendations:
            st.write("👉", movie)
