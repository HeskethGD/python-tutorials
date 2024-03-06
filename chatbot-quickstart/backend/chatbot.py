from openai import OpenAI

def chatbot(openai_secret: dict, messages: list):
        
    system_message = """
    You are a helpful chatbot for answering investment based queries for hedge fund managers"""

    messages.append({
        "role": "system",
        "content": system_message
    })

    openai_client = OpenAI(api_key=openai_secret["apikey"])

    stream = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True
    )

    for chunk in stream:
        choice = chunk.choices[0]
        if not choice.finish_reason:
            yield choice.delta.content