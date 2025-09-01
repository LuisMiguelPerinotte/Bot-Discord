import logging
import os
from datetime import datetime
import requests

# Handler customizado Discord 
WEBHOOK_URL = os.getenv("WEBHOOK_DISCORD_LOG")

class DiscordWebhookHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        try:
            requests.post(WEBHOOK_URL, json={"content": f"```{log_entry}```"})
        except Exception as e:
            print("Falha ao enviar log para Discord:", e)

# Logs locais 
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"uso_comando_{datetime.now().strftime('%Y-%m-%d')}.txt")

# Cria o logger central
logger = logging.getLogger("bot_logger")
logger.setLevel(logging.INFO)

# Handler arquivo local
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.INFO)

# Handler Discord 
discord_handler = DiscordWebhookHandler()
discord_handler.setLevel(logging.INFO)

# Formatação
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
discord_handler.setFormatter(formatter)

# Adiciona os dois handlers
logger.addHandler(file_handler)
logger.addHandler(discord_handler)

# Função de atalho
def registrar_uso_comando(info):
    logger.info(info)
