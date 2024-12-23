import requests
import os
from dotenv import load_dotenv


class AuthenticationService:

    def __init__(self):
        load_dotenv()
        self.__base_url = os.getenv("BASE_URL")
        self.__auth_url = f"{self.__base_url}authentication/token/"

    def get_token(self, username, password):
        response = requests.post(
            self.__auth_url, data={"username": username, "password": password}
        )
        if response.status_code == 200:
            return response.json()
        return {"error": f"Erro ao autenticar. Status Code {response.status_code}"}
