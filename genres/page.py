import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


genres = [
    {
        "id": 1,
        "name": "Ação"
    },
    {
        "id": 2,
        "name": "Aventura"
    },
    {
        "id": 3,
        "name": "Animação"
    }
]


def show_genres():
    st.title("Lista de gêneros")
    AgGrid(data=pd.DataFrame(genres), reload_data=True, key="genres_grid")
    st.title("Cadastrar novo gênero")

    genre_name = st.text_input("Nome do gênero")
    if st.button("Cadastrar"):
        st.success(f'Gênero "{genre_name}" cadastrado com sucesso')
