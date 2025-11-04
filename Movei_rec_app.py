import streamlit as st
from recommendation_system import get_hybrid_recommendations, recommend_movies

st.title("🎬 AI-Powered Movie Recommendation System")

st.info(
    "**Which Recommendation Model Should You Choose?**\n\n"
    "- **Hybrid (Best Choice)** → Uses user preferences & movie features for highly accurate results. 📊\n"
    "- **Content-Based Filtering** → Suggests movies based on genre similarities. 🎭"
)

rec_type = st.selectbox("Choose Recommendation Type:", 
                      ["Hybrid (CF + Content-Based)", "Content-Based Filtering"])

user_movie = st.text_input("Enter a movie name:")

if user_movie:
    st.subheader("🎬 Recommended Movies")
    
    if rec_type == "Hybrid (CF + Content-Based)":
        recommendations = get_hybrid_recommendations(user_movie)
    else:
        recommendations = recommend_movies(user_movie)
    
    if recommendations:
        for movie in recommendations:
            st.write(f"- {movie}")
    else:
        st.write("No recommendations found. Please try another movie title.")