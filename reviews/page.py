import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


genres = [
    {
        "id": 1,
        "stars": 5
    },
    {
        "id": 2,
        "stars": 4
    },
    {
        "id": 3,
        "stars": 3
    }
]


def show_reviews():
    st.title("Lista de avaliações")
    AgGrid(data=pd.DataFrame(genres), reload_data=True, key="reviews_grid")
