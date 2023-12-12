import os
import openai

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key: {api_key}")  # Esto imprimirá tu clave de API, asegúrate de que es correcta
openai.api_key = api_key

def crear_contenido (tema,tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Por favor escribe un articulo corto sobre el tema : {tema}\n\n"
    respuesta= openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=temperatura,
        max_tokens=tokens
    )
    return respuesta.choices[0].text.strip()

# Ejemplo de uso
def resumir_text(texto,tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Resume el siguiente texto en español: {texto}\n\n"
    respuesta= openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=temperatura,
        max_tokens=tokens
    )
    return respuesta.choices[0].text.strip()

tema=input("Elija un tema para el articulo: ")
tokens=int(input("Cuantos Tokens Maximo va tener tu articulo: "))
temperatura=int(input("del 1 al 10, que tan creativo quieres que sea tu articulo: "))/10
articulo_creado=crear_contenido(tema,tokens,temperatura)
print(articulo_creado)

tema=input("Pega aqui el articulo que quieres resumir: ")
tokens=int(input("Cuantos Tokens Maximo va tener tu resumen: "))
temperatura=int(input("del 1 al 10, que tan creativo quieres que sea tu resumen: "))/10
resumen_creado=resumir_text(tema,tokens,temperatura)
print(resumen_creado)