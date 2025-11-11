# app.py
import os
import gradio as gr
from huggingface_hub import InferenceClient

HF_TOKEN = os.environ.get("HF_TOKEN")
client = InferenceClient(token=HF_TOKEN)

def responder(mensagem):
    try:
        response = client.chat_completion(
            model="zai-org/GLM-4.6:novita",  # modelo de chat real
            messages=[
                {"role": "system", "content": "Você é uma atendente simpática e empática que fala português de forma natural."},
                {"role": "user", "content": mensagem}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Houve um erro ao gerar resposta: {e}"

with gr.Blocks() as demo:
    gr.Markdown("## Atendente Virtual WhatsApp")
    chat = gr.Chatbot()
    msg = gr.Textbox(label="Digite sua mensagem")
    clear = gr.Button("Limpar")

    def enviar(msg_text, chat_history):
        resposta = responder(msg_text)
        chat_history.append((msg_text, resposta))
        return chat_history, ""

    msg.submit(enviar, [msg, chat], [chat, msg])
    clear.click(lambda: [], None, chat)

demo.launch()
