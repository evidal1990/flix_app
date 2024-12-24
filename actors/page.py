import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from actors.service import ActorService
from datetime import datetime


def show_actors():
    actor_service = ActorService()

    # Lista de atores cadastrados
    with st.container():
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

    # Cadastro do usuário
    with st.container():
        st.title("Cadastrar novo ator ou atriz")

        name = st.text_input("Nome do ator/atriz")
        birthday = st.date_input(
            label="Data de nascimento",
            value=datetime.today(),
            min_value=datetime(1900, 1, 1).date(),
            max_value=datetime.today(),
            format="DD/MM/YYYY"
        )

        nationalities_options = actor_service.get_nationalities()
        nationality_value = st.selectbox(
            label="Nacionalidade",
            options=nationalities_options,
        )

        nationality_key = actor_service.get_nationality_key(nationality_value)

        if st.button("Cadastrar"):
            created_actor = actor_service.create_actor(
                name=name,
                birthday=birthday,
                nationality=nationality_key,
            )
            if created_actor:
                st.success(f'Ator/Atriz "{input}" cadastrado(a) com sucesso')
                st.rerun()
            else:
                st.error("Erro ao cadastrar ator/atriz. Verifique os campos")
