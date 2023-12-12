import os
import openai

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key: {api_key}")  # Esto imprimirá tu clave de API, asegúrate de que es correcta
openai.api_key = api_key

preguntas_anteriores= []
respuestas_anteriores=[]

def preguntar_chat_gpt (prompt, modelo="text-davinci-002"):
    respuesta= openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=0.5,
        max_tokens=100
    )
    return respuesta.choices[0].text.strip()

print("Bienvenido a nuestro chatBot Basico. Escribe 'salir' cuando quieras terminar")
while True:
    conversacion_historica=""
    ingreso_usuario=input("\nTu:")
    if ingreso_usuario.lower()=="salir":
        break

    for pregunta, respuesta in zip(preguntas_anteriores,respuestas_anteriores):
        conversacion_historica += f"El usuario pregunta : {pregunta} \n"
        conversacion_historica += f"Mi ChatGPT Responde: {respuesta}\n"

    prompt =f"El Usuario pregunta: {ingreso_usuario}\n"
    conversacion_historica+=prompt
    respuesta_gpt=preguntar_chat_gpt(conversacion_historica)
    print(f"{respuesta_gpt}")

    preguntas_anteriores.append(ingreso_usuario)
    respuestas_anteriores.append(respuesta_gpt)