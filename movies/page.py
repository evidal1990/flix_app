import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from movies.service import MovieService


def show_movies():
    movie_service = MovieService()

    with st.container():
        movies = movie_service.get_movies()
        if movies:
            st.title("Lista de filmes")
            AgGrid(
                data=pd.json_normalize(movies),
                reload_data=True,
                key="movies_grid"
            )
        else:
            st.warning("Nenhum filme cadastrado")

    with st.container():
        st.title("Cadastrar novo filme")
        movie_name = st.text_input("Nome do filme")
        if st.button("Cadastrar"):
            st.success(f'Filme "{movie_name}" cadastrado com sucesso')
