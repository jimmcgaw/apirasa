import requests
import http.client

from django.conf import settings

host = settings.RASA_CHATSERVER_HOST
port = settings.RASA_CHATSERVER_PORT
endpoint = settings.RASA_CHATSERVER_ENDPOINT

RASA_URL = f"http://{host}:{port}"
RASA_CHAT_URL = f"{RASA_URL}{endpoint}"

class Rasa:
    def hello(say):
        response = requests.get(RASA_URL)
        raise Exception(response.text)

    def say(self, message):
        data = {
            "message": message,
            "sender": "django"
        }
        headers = {'content-type' : 'application/json'}
        response = requests.post(RASA_CHAT_URL, headers=headers, json=data)
        if response.status_code == http.client.OK:
            return response.json()
        else:
            response.raise_for_status()