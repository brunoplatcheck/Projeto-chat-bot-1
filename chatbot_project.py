# -*- coding: utf-8 -*-
"""chatbot_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B95GcpBsbWtyCqB0sv05QthZQwuIPl59
"""

!pip install google-genai

import os
from google.colab import userdata

os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')

from google import genai

client=genai.Client()

for model in client.models.list():
  print(model.name)

modelo="gemini-2.0-flash"

response=client.models.generate_content(model=modelo, contents="Oi tudo bem?")

response.text

chat=client.chats.create(model=modelo)

resposta=chat.send_message("Oi tudo bem?")

resposta.text

resposta=chat.send_message(" o que é inteligencia artificial")

resposta.text

from google.genai import types

chat_config=types.GenerateContentConfig(
    system_instruction="Voce é um assistente pessoal e sempre responde de forma sucinta.",
)

chat=client.chats.create(model=modelo, config=chat_config)

resposta=chat.send_message("o que é inteligencia artificial")

resposta.text

chat.get_history()

prompt=input('Esperando prompt: ')

while prompt !="fim":
  resposta=chat.send_message(prompt)
  print("Resposta: ",resposta.text)
  print("\n\n")
  prompt=input('Esperando prompt: ')

chat.get_history()

chat_config_2=types.GenerateContentConfig(
    system_instruction="voce é um assistente pessoal que sempre responde de forma muito sarcastica",
)

chat_2=client.chats.create(model=modelo, config=chat_config)

from google.colab import drive
drive.mount('/content/drive')

prompt=input('Esperando prompt: ')

while prompt !="fim":
  resposta=chat_2.send_message(prompt)
  print("Resposta: ",resposta.text)
  print("\n\n")
  prompt=input('Esperando prompt: ')