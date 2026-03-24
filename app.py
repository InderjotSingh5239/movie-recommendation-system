import streamlit as st
import pandas as pd
import time
from model import recommend

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# DARK THEME CSS
# -----------------------------
st.markdown("""
<style>
/* Full App Background */
.stApp {
    background-color: #0d1117;
    color: #ffffff;
}

/* Title */
h1 {
    text-align: center;
    color: #ff4b4b;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161b22;
}

/* Movie Cards */
.movie-card {
    background-color: #161b22;
    padding: 15px;
    border-radius: 12px;
    margin: 10px 0;
    transition: 0.3s;
    box-shadow: 0px 0px 10px rgba(255, 75, 75, 0.2);
}

.movie-card:hover {
    transform: scale(1.03);
    background-color: #21262d;
}

/* Button Styling */
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

/* Dropdown */
.stSelectbox label {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown("<h1>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Find movies based on your favorite genre</p>", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("movies.csv")

movies = load_data()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🎬 Movie App")
st.sidebar.markdown("Choose your preference")

genres = movies["genre"].dropna().unique()
selected_genre = st.sidebar.selectbox("Select Genre", genres)

# -----------------------------
# BUTTON ACTION
# -----------------------------
if st.sidebar.button("🎯 Recommend Movies"):

    with st.spinner("🔍 Finding best movies for you..."):
        time.sleep(1)
        recommendations = recommend(selected_genre)

    st.subheader(f"🎥 Top {selected_genre} Movies")

    if len(recommendations) == 0:
        st.warning("No movies found for this genre.")
    else:
        for movie in recommendations:
            st.markdown(f"""
            <div class="movie-card">
                <h3>🎬 {movie}</h3>
            </div>
            """, unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("<p style='text-align:center;'>Made by Inderjot Singh 🚀</p>", unsafe_allow_html=True)
