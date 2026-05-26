import google.generativeai as genai
from dotenv import load_dotenv
import os
import PIL.Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

img = PIL.Image.open('animais.jpg')

prompt = """Essa imagem contém uma série de animais desenhados. Existem cinco linhas.
As primeiras quatro linhas possuem seis animais. A última linha possui oito animais.
Liste os animais que você encontrou no formato JSON, sendo que cada objeto deve conter
o nome do animal, sua classificação (mamífero, réptil, etc) e o som que ele faz. O resultado
deve vir no idioma português do Brasil."""

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content([prompt, img])
print(response.text)