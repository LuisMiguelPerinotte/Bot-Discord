import os, requests, logging
from datetime import datetime

# Handler customizado para Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/1411816186135707658/DevRJcrIOBuxnfE5Ye47jg8fVFd-efYFHvFRL8pbWcoGuGCQrt78vIHtMxPb_8ZFALo1"

class DiscordWebhookHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        try:
            requests.post(WEBHOOK_URL, json={"content": f"```{log_entry}```"})
        except Exception as e:
            print("Falha ao enviar log para Discord:", e)

# Criar pastas se não existir
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"uso_comando_{datetime.now().strftime('%Y-%m-%d')}.txt")


# Logger central
logger = logging.getLogger("bot_logger")
logger.setLevel(logging.INFO)


# Handler arquivo local
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.INFO)


# Handler discord
discord_handler = DiscordWebhookHandler()
discord_handler.setLevel(logging.INFO)


# Formatação
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
discord_handler.setFormatter(formatter)


# Adiciona os dois handlers
logger.addHandler(file_handler)
logger.addHandler(discord_handler)


def registrar_uso_comando(info):
    logging.info(info)