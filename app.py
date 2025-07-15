import pickle

import pandas as pd
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie,val):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:val+1]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies_dict= pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)

movie_list = movies['title'].values
col_search, col_slider = st.columns([2, 1])

with col_search:
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

with col_slider:
    value = st.number_input('How many movies to recommend?', min_value=1, max_value=10, value=5, step=1)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie, value)

    if len(recommended_movie_names) < value:
        st.warning("Fewer recommendations available than requested.")

    # Show recommendations in rows of 5 columns
    for row_start in range(0, len(recommended_movie_names), 5):
        cols = st.columns(5)
        for i in range(5):
            idx = row_start + i
            if idx < len(recommended_movie_names):
                with cols[i]:
                    st.text(recommended_movie_names[idx])
                    st.image(recommended_movie_posters[idx])
