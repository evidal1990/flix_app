import requests


class AuthenticationService:

    def __init__(self):
        self.__base_url = "https://evidal1990.pythonanywhere.com/api/v1/"
        self.__auth_url = f"{self.__base_url}authentication/token/"

    def get_token(self, username, password):
        response = requests.post(
            self.__auth_url, data={"username": username, "password": password}
        )
        if response.status_code == 200:
            return response.json()
        return {"error": f"Erro ao autenticar. Status Code {response.status_code}"}
