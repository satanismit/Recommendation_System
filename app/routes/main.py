import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

# Set page config
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="��",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        padding: 1rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        min-height: 100vh;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #FF4B4B, #FF7676);
        color: white !important;
        font-size: 1.2rem;
        font-weight: 600;
        padding: 1rem;
        border-radius: 15px;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        transition: all 0.3s ease;
        text-transform: none;
        letter-spacing: 0.5px;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.4);
    }
    
    .movie-card {
        background: white;
        padding: 1.5rem;
        margin: 0.5rem 0;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .movie-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }
    
    .title {
        color: #1E1E1E;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-align: center;
        line-height: 1.2;
    }
    
    .subtitle {
        color: #666;
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 1.5rem;
        line-height: 1.4;
    }
    
    .selectbox-container {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
    }
    
    .recommendations-title {
        color: #1E1E1E;
        font-size: 1.8rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
        text-align: center;
    }
    
    .stSelectbox > div {
        background: white;
    }
    
    /* Remove extra spacing */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    /* Fix button text display */
    .stButton > button > div {
        color: white !important;
        font-weight: 600;
    }
    
    /* Optimize overall spacing */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Remove default margins */
    .stMarkdown {
        margin-bottom: 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description with enhanced styling
st.markdown('<h1 class="title">🎬 Movie Recommendation System</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Discover your next favorite movie with our intelligent recommendation system!</p>', unsafe_allow_html=True)

# Add a small spacer to reduce white space
st.markdown('<div style="height: 0.5rem;"></div>', unsafe_allow_html=True)

# Load movie data from pickle files
@st.cache_data
def load_movie_data():
    artifacts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'artifacts')
    
    with open(os.path.join(artifacts_dir, 'movies_pivot.pkl'), 'rb') as f:
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

    # Movie selection in a styled container
    st.markdown('<div class="selectbox-container">', unsafe_allow_html=True)
    selected_movie = st.selectbox(
        "🎯 Select a movie you like:",
        ratings.index.tolist()
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Add a small spacer before the button
    st.markdown('<div style="height: 0.5rem;"></div>', unsafe_allow_html=True)

    if st.button("✨ Get Recommendations", key="recommend_btn"):
        st.markdown('<h2 class="recommendations-title">🎯 Recommended Movies</h2>', unsafe_allow_html=True)
        recommendations = get_recommendations(selected_movie)
        
        # Create a container for recommendations
        with st.container():
            for i, movie in enumerate(recommendations, 1):
                st.markdown(f"""
                <div class="movie-card">
                    <h3 style='margin: 0; color: #1E1E1E; font-size: 1.1rem;'>
                        <span style='color: #FF4B4B; font-weight: 700;'>{i}.</span> {movie}
                    </h3>
                </div>
                """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"Error loading movie data: {str(e)}")
    st.info("Please make sure the pickle files are present in the artifacts folder.") 