import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from movies.service import MovieService
from actors.service import ActorService
from genres.service import GenreService


def show_movies():
    movie_service = MovieService()
    genre_service = GenreService()

    with st.container():
        movies = movie_service.get_movies()

        if not movies:
            st.warning("Nenhum filme cadastrado")
        else:
            for movie in movies:
                movie["genre"] = genre_service.get_genre_by_id(movie["genre"])
            movies_df = pd.json_normalize(movies)
            movies_df = movies_df.drop(columns=["actors"])

            st.title("Lista de filmes")
            AgGrid(
                data=movies_df,
                reload_data=True,
                key="movies_grid"
            )

    with st.container():
        st.title("Cadastrar novo filme")

        title = st.text_input("Título do filme")

        release_date = st.date_input(
            label="Data de lançamento",
            value=datetime.today(),
            min_value=datetime(1900, 1, 1).date(),
            max_value=datetime.today(),
            format="DD/MM/YYYY"
        )

        genres = genre_service.get_genres_name()
        selected_genre = st.selectbox(
            "Gênero",
            list(genres.keys())
        )

        actor_service = ActorService()
        actors = actor_service.get_actors_name()
        selected_actors_name = st.multiselect(
            "Atores",
            list(actors)
        )

        resume = st.text_area("Resumo")

        if st.button("Cadastrar"):
            new_movie = movie_service.create_movie(
                title=title,
                release_date=release_date,
                genre=genres[selected_genre],
                actors=[actors[name] for name in selected_actors_name],
                resume=resume
            )
            if new_movie:
                st.success(f'Filme "{title}" cadastrado com sucesso')
                st.rerun()
            else:
                st.error("Erro ao cadastrar o filme. Verifique os campos")
