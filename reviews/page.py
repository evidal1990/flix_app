import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews():
    review_service = ReviewService()

    with st.container():
        reviews = review_service.get_reviews()
        if not reviews:
            st.warning("Nenhuma avaliação encontrada")
        else:
            st.title("Lista de avaliações")
            AgGrid(
                data=pd.DataFrame(pd.json_normalize(reviews)),
                reload_data=True,
                key="reviews_grid"
            )

    with st.container():
        movie_service = MovieService()
        movies = movie_service.get_movies()
        if not movies:
            st.warning("Nenhum filme a ser avaliado")
        else:
            st.title("Cadastrar nova avaliação")

            movie_titles = {movie["title"]: movie["id"] for movie in movies}
            selected_movie = st.selectbox(
                "Filme",
                list(movie_titles.keys())
            )

            selected_star = st.number_input(
                label="Estrelas",
                min_value=1,
                max_value=5,
                step=1
            )

            comment = st.text_area("Comentário")

            if st.button("Cadastrar"):
                new_review = review_service.create_review(
                    movie=movie_titles[selected_movie],
                    stars=selected_star,
                    comment=comment
                )
                if new_review:
                    st.success("Review cadastrado com sucesso")
                    st.rerun()
                else:
                    st.error("Erro ao cadastrar avaliação. Verifique os campos")
