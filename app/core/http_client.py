import requests
from app.core.settings import settings

def fetch_data(endpoint: str):

    url = f"{settings.URL_API_SS}/{endpoint}"

    try:
        response = requests.get(url)
        print(f"Resposta HTTP: {response.status_code}")
        print(f"Resposta bruta: {response.text}")

        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(e)
