import streamlit as st
import os
import requests
from dotenv import load_dotenv
from login.service import logout


class MovieRepository:

    def __init__(self):
        load_dotenv()
        self.__base_url = os.getenv("BASE_URL")
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            "Authorization": f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(self.__movies_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code {response.status_code}')

    def create_movie(self, movie):
        response = requests.get(self.__movies_url, headers=self.__headers, data=movie)
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code {response.status_code}')
