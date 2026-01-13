from pathlib import Path
from datetime import datetime


class Logger:
    LOG_DIR = Path("logs")
    ERRO_FILE = LOG_DIR / "erro.txt"
    INFO_FILE = LOG_DIR / "info.txt"

    @staticmethod
    def _criar_diretorio():
        """Cria o diretório de logs se não existir."""
        Logger.LOG_DIR.mkdir(exist_ok=True)

    @staticmethod
    def escrever_log_erro(mensagem):
        """Escreve mensagem de erro em arquivo separado."""
        Logger._criar_diretorio()
        with open(Logger.ERRO_FILE, "a", encoding="utf-8") as log:
            log.write(f"[{datetime.now():%d/%m/%Y %H:%M:%S}] {mensagem}\n")

    @staticmethod
    def escrever_log_info(mensagem):
        """Escreve mensagem de informação em arquivo separado."""
        Logger._criar_diretorio()
        with open(Logger.INFO_FILE, "a", encoding="utf-8") as log:
            log.write(f"[{datetime.now():%d/%m/%Y %H:%M:%S}] {mensagem}\n")

    @staticmethod
    def escrever_log_sucesso(mensagem):
        """Escreve mensagem de sucesso (alias para info)."""
        Logger.escrever_log_info(mensagem)