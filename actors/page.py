import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


actors = [
    {
        "id": 1,
        "name": "Leonardo DiCaprio"
    },
    {
        "id": 2,
        "name": "Silverster Stallone"
    },
    {
        "id": 3,
        "name": "Meryl Streep"
    }
]


def show_actors():
    st.title("Lista de atores/atrizes")
    AgGrid(data=pd.DataFrame(actors), reload_data=True, key="actors_grid")
    st.title("Cadastrar novo ator ou atriz")

    actor_name = st.text_input("Nome do ator/atriz")
    if st.button("Cadastrar"):
        st.success(f'Ator/Atriz "{actor_name}" cadastrado com sucesso')
