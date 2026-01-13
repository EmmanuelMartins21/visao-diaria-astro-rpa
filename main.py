
from services.nasa_api_service import NasaApiService

from utils.config import config
from services.image_service import baixar_imagem

from repository.image_repository import ImageRepository
service = NasaApiService(
    base_url=config["nasa_api"]["base_url"],
    api_key=config["nasa_api"]["api_key"]
)
repository = ImageRepository()

imagem = service.get_apod()
url = imagem.url
data_imagem = imagem.data
titulo_imagem = imagem.titulo

print("Dados da APOD obtidos com sucesso.")
print(f"Título: {titulo_imagem}")
print(f"URL: {url}")
print(f"Data: {data_imagem}")


if url.endswith(('.jpg', '.jpeg', '.png')):
    baixar_imagem(url, data_imagem, titulo_imagem)


repository.salvar_imagem(imagem)

print(imagem.url)
