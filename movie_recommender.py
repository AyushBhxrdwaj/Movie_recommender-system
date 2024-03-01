import streamlit as st
import pickle
import pandas as pd
import requests
import requests


def fetch_movie_posters(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=c8b5809543e9c2079ce290f90c34fdd5&language=en-US".format(movie_id
            
        )
    )
    d = response.json()
    return "https://image.tmdb.org/t/p/w500/" + d['poster_path']


movies_list = pickle.load(
    open(
        "C:/Users/91956/Dropbox/PC/Desktop/python/python/MachineLearning/movies_dict.pkl",
        "rb",
    )
)
data = pd.DataFrame(movies_list)
st.title("Movie Recommender System")
details = st.selectbox("What do you want to see?", data["title"].values)
similarity = pickle.load(
    open(
        "C:/Users/91956/Dropbox/PC/Desktop/python/python/MachineLearning/similarity.pkl",
        "rb",
    )
)


def recommend(movie):
    movie_index = data[data["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6
    ]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        recommended_movies.append((data["title"].iloc[i[0]]))
        movie_id = data["id"].iloc[i[0]]
        recommended_movies_poster.append(fetch_movie_posters(movie_id))
    return recommended_movies,recommended_movies_poster


if st.button("Recommend"):
    names, posters = recommend(details)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])
