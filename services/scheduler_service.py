from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from utils.logger import Logger


class Scheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
    
    def agendar_execucao_diaria(self, funcao, hora: int = 20, minuto: int = 0):
       
        try:
            trigger = CronTrigger(hour=hora, minute=minuto)
            self.scheduler.add_job(
                funcao,
                trigger=trigger,
                id='apod_diario',
                name=f'Execução APOD às {hora:02d}:{minuto:02d}',
                replace_existing=True
            )
            Logger.escrever_log_info(f"Agendamento criado para {hora:02d}:{minuto:02d}")
        except Exception as e:
            Logger.escrever_log_erro(f"Erro ao agendar execução: {e}")
            raise
    
    def iniciar(self):
        if not self.scheduler.running:
            self.scheduler.start()
            Logger.escrever_log_info("Scheduler iniciado")
    
    def parar(self):
        if self.scheduler.running:
            self.scheduler.shutdown()
            Logger.escrever_log_info("Scheduler parado")
