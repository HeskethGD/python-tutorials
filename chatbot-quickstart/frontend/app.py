import gradio as gr
import requests

base_url = "http://localhost:8000"
url_ext = "streaming/data_chat"
url = f"{base_url}/{url_ext}"


def chat_response(message, history):

    # Transform gradio inputs to OpenAI style messages
    messages = []
    for pair in history:
        messages.append({
            "role": "user",
            "content": pair[0]
        })
        messages.append({
            "role": "assistant",
            "content": pair[1]
        })

    messages.append({
            "role": "user",
            "content": message
        })

    partial_message = ""
    with requests.post(url, json={"messages": messages}, stream=True) as r:
        for chunk in r.iter_content(None, decode_unicode=True):
            if chunk:
                partial_message += chunk
                yield partial_message
                
gr.ChatInterface(chat_response).launch()


