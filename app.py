import streamlit as st


def main():
    st.title("Flix App")

    menu_options = st.sidebar.selectbox(
        "Selecione uma opção",
        ["Início", "Gêneros", "Atores/Atrizes", "Filmes", "Avaliações"]
    )

    create_menu_options(menu_options)


def create_menu_options(menu_options):

    match menu_options:
        case "Início":
            st.write("Seja bem-vindo ao Flix App!")
        case "Gêneros":
            st.write("Gêneros de filmes")
        case "Atores/Atrizes":
            st.write("Atores e atrizes")
        case "Filmes":
            st.write("Filmes")
        case "Avaliações":
            st.write("Avaliações")


if __name__ == "__main__":
    main()
