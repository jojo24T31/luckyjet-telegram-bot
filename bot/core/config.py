import os
from dotenv import load_dotenv

load_dotenv()

# 🔐 Variables sensibles
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# 🌐 Configuration du scraping
ENDPOINT_URL = os.getenv("ENDPOINT_URL")
USER_AGENT = os.getenv("USER_AGENT", "Mozilla/5.0")
