import streamlit as st


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
    st.table(genres)
    st.title("Cadastrar novo gênero")

    genre_name = st.text_input("Nome do gênero")
    if st.button("Cadastrar"):
        st.success(f'Gênero "{genre_name}" cadastrado com sucesso')
