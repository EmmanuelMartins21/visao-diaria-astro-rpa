from services.nasa_api_service import NasaApiService
import json

def carregar_configuracoes() -> dict:
    # Carregando as configurações do arquivo settings.json
    with open('config/settings.json', 'r', encoding='utf-8') as f:
        return json.load(f)

config = carregar_configuracoes()