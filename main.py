from services.scheduler_service import Scheduler
from main import executar_apod
import signal
import sys

from utils.logger import Logger

def executar_apod():
    """Função que executa a coleta e envio do APOD."""
    from services.nasa_api_service import NasaApiService
    from utils.config import config
    from services.image_service import baixar_imagem
    from repository.image_repository import ImageRepository
    
    try:
        service = NasaApiService(
            base_url=config["nasa_api"]["base_url"],
            api_key=config["nasa_api"]["api_key"]
        )
        repository = ImageRepository()
        
        imagem = service.get_apod()
        
        if imagem.url and imagem.url.endswith(('.jpg', '.jpeg', '.png')):
            baixar_imagem(imagem.url, imagem.data, imagem.titulo)
        
        repository.salvar_imagem(imagem)
        Logger.escrever_log_info(f"✓ APOD executado com sucesso: {imagem.titulo}")
        
    except Exception as e:
        Logger.escrever_log_erro(f"✗ Erro ao executar APOD: {e}")


def main():
    scheduler = Scheduler()
    scheduler.agendar_execucao_diaria(executar_apod, hora=20, minuto=0)
    scheduler.iniciar()
    
    # Permite parar com Ctrl+C
    def handler(signum, frame):
        scheduler.parar()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, handler)
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        scheduler.parar()


if __name__ == "__main__":
    main()