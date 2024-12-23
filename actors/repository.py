import streamlit as st
import os
import requests
from dotenv import load_dotenv
from login.service import logout


class ActorRepository:

    def __init__(self):
        load_dotenv()
        self.__base_url = os.getenv("BASE_URL")
        self.__genres_url = f'{self.__base_url}actors/'
        self.__headers = {
            "Authorization": f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(self.__genres_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code {response.status_code}')

    def create_actor(self, actor):
        response = requests.post(self.__genres_url, headers=self.__headers, data=actor)
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status Code {response.status_code}')
