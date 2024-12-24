import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from actors.service import ActorService
from datetime import datetime


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()
    if actors:
        st.title("Lista de atores/atrizes")
        AgGrid(
            data=pd.DataFrame(pd.json_normalize(actors)),
            reload_data=True,
            key="actors_grid"
        )
    else:
        st.warning("Nenhum(a) ator/atriz encontrado(a)")

    st.title("Cadastrar novo ator ou atriz")
    actor_name = st.text_input("Nome do ator/atriz")
    actor_birthday = st.date_input(
        label="Data de nascimento",
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format="DD/MM/YYYY"
    )
    nationalities_options = actor_service.get_nationalities()
    actor_nationality = st.selectbox(
        label="Nacionalidade",
        options=nationalities_options,
    )
    if st.button("Cadastrar"):
        new_actor = actor_service.create_actor(
            name=actor_name,
            birthday=actor_birthday,
            nationality=actor_nationality,
        )
        if new_actor:
            st.success(f'Ator/Atriz "{actor_name}" cadastrado(a) com sucesso')
            st.rerun()
        else:
            st.error("Erro ao cadastrar ator/atriz. Verifique os campos")
