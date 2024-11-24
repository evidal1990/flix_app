import streamlit as st
from genres.page import show_genres


def main():
    menu_options = st.sidebar.selectbox(
        "Selecione uma opção",
        ["Início", "Gêneros", "Atores/Atrizes", "Filmes", "Avaliações"]
    )

    if menu_options == "Início":
        st.title("Seja bem-vindo ao Flix App!")

    if menu_options == "Gêneros":
        show_genres()

    if menu_options == "Atores/Atrizes":
        st.title("Atores/Atrizes")

    if menu_options == "Filmes":
        st.title("Filmes")

    if menu_options == "Avaliações":
        st.title("Avaliações")


if __name__ == "__main__":
    main()
