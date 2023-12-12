import os
import openai

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key: {api_key}")  # Esto imprimirá tu clave de API, asegúrate de que es correcta
openai.api_key = api_key

def traducir_texto(texto, idioma):
    modelo="text-davinci-002"
    prompt = f"Traduce el texto '{texto}' la {idioma}."

    respuesta= openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=1,
        max_tokens=100
    )
    return respuesta.choices[0].text.strip()

mi_texto= input("Ingresa el texto a traducir")
lenguaje=input("¿Cuál lenguaje deseas traducir?")
traducir= traducir_texto(mi_texto,lenguaje)
print(traducir)