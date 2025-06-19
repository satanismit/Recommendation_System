import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

#Setup
st.set_page_config(
    page_title="🎬 Movie Recommendation System",
    page_icon="🎞️",
    layout="wide",
)

#Session State 
if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

if "watchlist" not in st.session_state:
    st.session_state.watchlist = []

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# ------------- Theme Toggle ----------
theme = st.radio("🌓 Choose Theme:", ["dark", "light"], horizontal=True)
st.session_state.theme = theme

# Dynamic CSS
if theme == "dark":
    bg_color = "#0f1117"
    text_color = "#FFFFFF"
    box_bg = "#1f1f2e"
    accent = "#00bcd4"
else:
    bg_color = "#f5f5f5"
    text_color = "#1e1e1e"
    box_bg = "#ffffff"
    accent = "#1976d2"

st.markdown(f"""
    <style>
    html, body, [class*="css"] {{
        font-family: 'Montserrat', sans-serif;
        background-color: {bg_color};
        color: {text_color};
    }}

    .stApp {{
        background-color: {bg_color};
    }}

    .title {{
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        color: {accent};
        margin-bottom: 0.2rem;
    }}

    .subtitle {{
        font-size: 1.1rem;
        text-align: center;
        color: #b0bec5;
        margin-bottom: 2rem;
    }}

    .selectbox-container {{
        background-color: {box_bg};
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
    }}

    .recommendations-title {{
        text-align: center;
        font-size: 1.6rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1.2rem;
        color: {accent};
    }}

    .chip {{
        background-color: {box_bg};
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        color: {accent};
        font-weight: 500;
        font-size: 0.95rem;
        box-shadow: 0 0 5px rgba(0, 229, 255, 0.05);
    }}

    .watchlist-chip {{
        background-color: {accent};
        color: white;
        margin: 0.2rem;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
    }}
    </style>
""", unsafe_allow_html=True)


st.markdown('<h1 class="title">🎬 Movie Recommendation System</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Discover your next favorite movie with our intelligent recommendation engine ✨</p>', unsafe_allow_html=True)

# Load Movie Data 
@st.cache_data
def load_movie_data():
    file_path = os.path.join("artifacts", "movies_pivot.pkl")
    with open(file_path, "rb") as f:
        ratings = pickle.load(f)
    return ratings

try:
    ratings = load_movie_data()
    similarity = cosine_similarity(ratings)

    def get_recommendations(movie_name):
        movie_index = ratings.index.get_loc(movie_name)
        distances = similarity[movie_index]
        similar_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        return [ratings.index[i[0]] for i in similar_movies]

    # Movie Selection Box
    st.markdown('<div class="selectbox-container">', unsafe_allow_html=True)
    selected_movie = st.selectbox("🎯 Select a movie you like:", ratings.index.tolist())
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        if st.button("✨ Get Recommendations"):
            st.session_state.recommendations = get_recommendations(selected_movie)

    with col2:
        if st.button("🗑 Clear Recommendations"):
            st.session_state.recommendations = []

    # Show Recommendations
    if st.session_state.recommendations:
        st.markdown('<h2 class="recommendations-title">🍿 Recommended Movies</h2>', unsafe_allow_html=True)
        for i, movie in enumerate(st.session_state.recommendations, 1):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f'<div class="chip">{i}. {movie}</div>', unsafe_allow_html=True)
            with col2:
                if st.button(f"➕ Add to Watchlist", key=f"add_{movie}"):
                    if movie not in st.session_state.watchlist:
                        st.session_state.watchlist.append(movie)

    # Show Watchlist
       # Show Watchlist
    if st.session_state.watchlist:
        st.markdown('<h2 class="recommendations-title">🎯 Your Watchlist</h2>', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; flex-wrap: wrap;">', unsafe_allow_html=True)
        for movie in st.session_state.watchlist:
            st.markdown(f'<div class="watchlist-chip">{movie}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Clear Watchlist Button
        if st.button("🗑 Clear Watchlist"):
            st.session_state.watchlist = []


except Exception as e:
    st.error(f"Error loading movie data: {str(e)}")
    st.info("Make sure the pickle files are correctly placed inside the 'artifacts' folder.")
