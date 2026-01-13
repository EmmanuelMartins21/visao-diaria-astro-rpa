import sqlite3
from typing import List, Optional
from model.imagem_nasa import imagem_nasa
from utils.logger import Logger


class ImageRepository:
 
    def __init__(self, db_path: str = "data/database.db"):

        self.db_path = db_path
        self._create_table()
    
    def _get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def _create_table(self) -> None:
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS imagens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT UNIQUE NOT NULL,
                    titulo TEXT NOT NULL,
                    url TEXT NOT NULL,
                    descricao TEXT
                )
            ''')
            
            conn.commit()
            conn.close()
        except Exception as e:
            Logger.escrever_log_erro(f"Erro ao criar tabela: {e}")
    
    def salvar_imagem(self, imagem: imagem_nasa) -> bool:        
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR REPLACE INTO imagens (data, titulo, url, descricao)
                VALUES (?, ?, ?, ?)
            ''', (imagem.data, imagem.titulo, imagem.url, imagem.descricao))
            
            conn.commit()
            conn.close()
            
            Logger.escrever_log_info(f"Imagem salva com sucesso: {imagem.titulo} ({imagem.data})")
            return True
            
        except Exception as e:
            Logger.escrever_log_erro(f"Erro ao salvar imagem: {e}")
            return False
    
    def buscar_imagem(self, data: str) -> Optional[imagem_nasa]:
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT data, titulo, url, descricao FROM imagens WHERE data = ?', (data,))
            row = cursor.fetchone()
            conn.close()
            
            if row:
                return imagem_nasa(
                    data=row[0],
                    titulo=row[1],
                    url=row[2],
                    descricao=row[3]
                )
            
            Logger.escrever_log_info(f"Imagem não encontrada para a data: {data}")
            return None
            
        except Exception as e:
            Logger.escrever_log_erro(f"Erro ao buscar imagem: {e}")
            return None
    
    def listar_imagens(self) -> List[imagem_nasa]:
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            cursor.execute('SELECT data, titulo, url, descricao FROM imagens ORDER BY data DESC')
            rows = cursor.fetchall()
            conn.close()
            
            imagens = [
                imagem_nasa(data=row[0], titulo=row[1], url=row[2], descricao=row[3])
                for row in rows
            ]
            
            Logger.escrever_log_info(f"Total de imagens no repositório: {len(imagens)}")
            return imagens
            
        except Exception as e:
            Logger.escrever_log_erro(f"Erro ao listar imagens: {e}")
            return []
