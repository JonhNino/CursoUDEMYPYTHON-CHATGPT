import os
import openai
import spacy

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key: {api_key}")  # Esto imprimirá tu clave de API, asegúrate de que es correcta
openai.api_key = api_key
modelos = openai.Model.list()
print(modelos)

modelo="text-davinci-002"
prompt = "Cuenta una historia Breve sobre un pais Europeo"

respuesta= openai.Completion.create(
    engine=modelo,
    prompt=prompt,
    n=3,
    temperature=1,
    max_tokens=100
)


texto_generado=respuesta.choices[0].text.strip()
print(texto_generado)

print("********")
print("********")
model_spacy_spanish=spacy.load("es_core_news_md")
analisis= model_spacy_spanish(texto_generado)

for token in analisis:
    print(token.text, token.pos_, token.dep, token.head.text)

for ent in analisis.ents:
    print(ent.text, ent.label_)

ubicacion=None

for ent in analisis.ents:
    if ent.label_ =="LOC":
        ubicacion=ent
        break
if ubicacion:
    prompt2=f"Dime mas acerca de {ubicacion}"
    respuesta2=openai.Completion.create(
         engine=modelo,
        prompt=prompt,
        n=3,
        temperature=1,
        max_tokens=100 
    )
    print(respuesta2.choices[0].text.strip())

