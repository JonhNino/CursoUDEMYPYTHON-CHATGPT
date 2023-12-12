import os
import openai

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key: {api_key}")  # Esto imprimirá tu clave de API, asegúrate de que es correcta
openai.api_key = api_key

def analizar_sentiemiento(texto)
    prompt="Por favor, analiza el sentimiento predominente en el siguiente texto: '{texto}'. El sentimeinto es: "
    respuesta= openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        temperature=0.5,
        max_tokens=100
    )
    return respuesta.choices[0].text.strip()

texto_para_analizar= input("Ingresa el texto")
sentimiento= analizar_sentiemiento(texto_para_analizar)
print(sentimiento)