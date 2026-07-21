import requests
from config import OLLAMA_URL, MODEL_NAME


def analyze_log(log_message):

    prompt = f"""

You are a Senior DevOps Engineer.

Analyze only this log:

{log_message}


Provide:

1. Possible Root Cause
2. Severity
3. Recommended Checks
4. Linux Commands


Do not invent information.

"""


    response = requests.post(

        OLLAMA_URL,

        json={

            "model": MODEL_NAME,

            "prompt": prompt,

            "stream": False

        },

        timeout=120

    )


    response.raise_for_status()


    return response.json()["response"]
