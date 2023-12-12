import os
import openai

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key: {api_key}")  # Esto imprimirá tu clave de API, asegúrate de que es correcta
openai.api_key = api_key
modelos = openai.Model.list()
print(modelos)

modelo="text-davinci-002"
prompt = "Resumen de la pelicula Matrix"

respuesta= openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=1,
    temperature=1,
    max_tokens=100
)

for idx,opcion in enumerate(respuesta.choices):
    texto_generado=opcion.text.strip()
    print(f"Respuesta {idx+1}: {texto_generado} \n")