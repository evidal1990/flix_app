import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.title("Lista de gêneros")
        AgGrid(
            data=pd.DataFrame(pd.json_normalize(genres)),
            reload_data=True,
            key="genres_grid"
        )
    else:
        st.warning("Nenhum gênero cadastrado")

    st.title("Cadastrar novo gênero")
    genre_name = st.text_input("Nome do gênero")
    if st.button("Cadastrar"):
        new_genre = genre_service.create_genre(name=genre_name)
        if new_genre:
            st.success(f'Gênero "{genre_name}" cadastrado com sucesso')
            st.rerun()
        else:
            st.error(f'Erro ao cadastrar gênero "{genre_name}"')
