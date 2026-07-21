import os
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv(
    "SLACK_WEBHOOK_URL"
)

LOG_FILE = "logs/server.log"

OLLAMA_URL = (
    "http://localhost:11434/api/generate"
)

MODEL_NAME = "tinyllama"
