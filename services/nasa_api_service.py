import requests
from datetime import datetime


from model.imagem_nasa import imagem_nasa

class NasaApiService:
    def __init__(self, base_url: str, api_key: str, timeout: int = 10):
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout

    def get_apod(self, date: str = None) -> imagem_nasa:
        params = {
            "api_key": self.api_key
        }

        if date:
            params["date"] = date

        try:
            response = requests.get(
                self.base_url,
                params=params,
                timeout=self.timeout
            )

            response.raise_for_status()
            data = response.json()
            print(data)

            return self._normalize_response(data)

        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao acessar a API da NASA: {e}")

    def _normalize_response(self, data: dict) -> imagem_nasa:
        return imagem_nasa(
            data=data.get("date"),
            titulo=data.get("title"),
            url=data.get("url") or data.get("hdurl"),
            descricao=data.get("explanation")
        )
    
