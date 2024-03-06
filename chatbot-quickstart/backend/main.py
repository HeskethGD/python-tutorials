from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from get_openai_secret import get_openai_secret
from chatbot import chatbot

app = FastAPI()

class Message(BaseModel):
    role: str
    content: str

class Body(BaseModel):
    messages: List[Message]

@app.post("/streaming/data_chat")
def api_chatbot(body: Body):
    """
    This function is a direct integration with ChatGPT with a simple system prompt for investments.
    It streams responses back to the UI.

    Parameters:
    - body (Body): contains the messages from the chat history
    - request (Request): contains the metadata for the request including headers used for auth

    Returns:
    - type: A Streaming response of the assistant message from ChatGPT.
    """

    messages = body.messages
    if messages == None or messages == []:
        return None

    try:

        openai_secret = get_openai_secret()
        return StreamingResponse(
            chatbot(openai_secret, messages), 
            media_type="text/html"
            )

    except HTTPException as e:
        raise HTTPException(status_code=500, detail="Internal server error")
