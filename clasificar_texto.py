import os
import openai

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key: {api_key}")  # Esto imprimirá tu clave de API, asegúrate de que es correcta
openai.api_key = api_key

def clasificar_texto(texto):
    categorias=[
        "arte",
        "ciencia",
        "deportes",
        "economia",
        "educacion",
        "entretenimiento"
    ]
    prompt=f"Por favor clasifica el siguiente texto '{texto}' en una de estas categorias{','.join(categorias)}. La categoria es:"
    respuesta= openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        temperature=0.5,
        max_tokens=50
    )
    return respuesta.choices[0].text.strip()

texto_clasificar=input("Ingrese un texto: ")
clasificacion= clasificar_texto(texto_clasificar)
print(clasificacion)
