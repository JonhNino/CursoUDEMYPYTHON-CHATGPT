import os
import openai

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key: {api_key}")  # Esto imprimirá tu clave de API, asegúrate de que es correcta
openai.api_key = api_key
modelos = openai.Model.list()
print(modelos)