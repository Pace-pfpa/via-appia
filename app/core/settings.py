import os
from dotenv import load_dotenv

dotenv_path = os.path.abspath(".env")
print(f"Carregando .env de: {dotenv_path}")
load_dotenv(dotenv_path)

class Settings:
        URL_API_SS:  str = os.getenv("URL_API_SS")
        LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")

        def __init__(self):
                print(f"URL_API_SS: {self.URL_API_SS}")

settings = Settings()