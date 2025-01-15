import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title("Estatística de filmes")

    print(movie_stats)

    with st.container():
        if len(movie_stats["movies_by_genre"]) == 0:
            st.error("Nenhum gráfico a ser exibido")
        else:
            fig = px.pie(
                movie_stats["movies_by_genre"],
                values="count",
                names="genre__name",
                title="Filmes por gênero"
            )
            st.plotly_chart(fig)

    with st.container():
        st.subheader("Total de filmes cadastrados")
        st.write(movie_stats["movies_total"])

    with st.container():
        st.subheader("Total de avaliações cadastradas")
        st.write(movie_stats["movies_reviews"])

    with st.container():
        st.subheader("Média geral de estrelas nas avaliações")
        st.write(movie_stats["movies_avg_stars"])
