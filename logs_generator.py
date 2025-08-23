import logging
import os
from datetime import datetime

# Criar pastas se não existir
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, f"uso_comando_{datetime.now().strftime('%Y-%m-%d')}.txt")

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,               # nível de log
    format="%(asctime)s - %(message)s",  # formato do log
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()      # opcional: imprime no console também
    ]
)

def registrar_uso_comando(info):
    logging.info(info)