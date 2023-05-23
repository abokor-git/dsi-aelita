import json
import gradio as gr
from fastapi import FastAPI
from EdgeGPT import Chatbot, ConversationStyle
import sys
import os
# Let's pick the desired backend
# os.environ['USE_TF'] = '1'
os.environ['USE_TORCH'] = '1'


CUSTOM_PATH = "/gradio"

app = FastAPI()


@app.get("/")
def read_main():
    return {"Home": "Bienvenue dans notre API de génération de texte (GPT). Cette API permet de discuter avec une ia en utilisant un modèle de machine learning GPT-4 de bing de microsoft entraîné pour cette tâche. Pour utiliser cette API, envoyez une requête POST ayant du texte en entrée. L'API renverra le texte génerer sous forme d'une réponse JSON. Pour utiliser cette API, veuillez vous référer à la documentation pour obtenir des instructions détaillées. N'hésitez pas à nous contacter si vous avez des questions ou des commentaires."}


async def treatment(text):

    with open('./cookies.json', 'r') as f:
        cookies = json.load(f)

    bot = Chatbot(cookies=cookies)

    response = await bot.ask(prompt=text, conversation_style=ConversationStyle.precise,
                             wss_link="wss://sydney.bing.com/sydney/ChatHub")

    return response["item"]["messages"][1]["text"]


demo = gr.Interface(
    fn=treatment,
    inputs=["text"],
    outputs=["text"],
)

app = gr.mount_gradio_app(app, demo, path=CUSTOM_PATH)

# Run this from the terminal as you would normally start a FastAPI app: `uvicorn api:app`
# and navigate to http://localhost:8000/gradio in your browser.
