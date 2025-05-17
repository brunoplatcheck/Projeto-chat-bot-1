
# 🤖 Projeto ChatBot com Google Gemini

Este projeto implementa um chatbot interativo utilizando a API da Google Gemini, por meio da biblioteca `google-genai`. O sistema simula conversas em tempo real com diferentes perfis de assistente: um padrão, um sucinto e outro com respostas sarcásticas.

> Projeto desenvolvido durante a Imersão IA da Alura, explorando o uso prático de modelos generativos.

## 💬 Funcionalidades

- 📥 Interface de prompt interativo via terminal
- 🧠 Chat com **modelo padrão**
- ✍️ Chat com **respostas sucintas**
- 😏 Chat com **respostas sarcásticas**
- 📜 Histórico de conversa com o modelo
- 🔐 Integração segura via `userdata.get('GOOGLE_API_KEY')` no Google Colab

## ⚙️ Tecnologias e Bibliotecas

- `google-genai`
- `Google Colab` (ambiente recomendado)

## 🧪 Como Executar

1. Abra o projeto no Google Colab.
2. Instale a biblioteca necessária:
   ```python
   !pip install google-genai
   ```
3. Configure sua chave de API da Google:
   ```python
   import os
   from google.colab import userdata
   os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')
   ```
4. Execute as células para interagir com o chatbot no terminal.

## 🧠 Exemplos de Uso

```python
prompt = input('Esperando prompt: ')

while prompt != "fim":
    resposta = chat.send_message(prompt)
    print("Resposta:", resposta.text)
    print("\n")
    prompt = input('Esperando prompt: ')
```

Você também pode trocar o `chat` para `chat_2` para ativar o modo sarcástico. 🧂

## 📁 Estrutura

```
├── chatbot_project.py           # Script principal do chatbot
├── chatbot_project.ipynb        # Notebook do Colab (versão interativa)
└── README.md                    # Este arquivo
```

## ⚠️ Observações

- Este projeto usa o modelo `gemini-2.0-flash`, que pode ser atualizado conforme novos modelos da API forem lançados.
- O sistema foi testado e idealizado para funcionar no ambiente do Google Colab.

## 👨‍💻 Autor

Desenvolvido por [Bruno Platcheck](https://github.com/brunoplatcheck) como parte dos estudos em IA generativa na Imersão IA da Alura.

---

🔗 [Acesse o repositório no GitHub](https://github.com/brunoplatcheck/Projeto-chat-bot-1)
