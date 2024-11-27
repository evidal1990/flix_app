import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


movies = [
    {
        "id": 1,
        "name": "Titanic"
    },
    {
        "id": 2,
        "name": "Creed"
    },
    {
        "id": 3,
        "name": "O Diabo Veste Prada"
    }
]


def show_movies():
    st.title("Lista de filmes")
    AgGrid(data=pd.DataFrame(movies), reload_data=True, key="movies_grid")
    st.title("Cadastrar novo filme")

    movie_name = st.text_input("Nome do filme")
    if st.button("Cadastrar"):
        st.success(f'Filme "{movie_name}" cadastrado com sucesso')
