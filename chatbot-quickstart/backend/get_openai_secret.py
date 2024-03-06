import os

def get_openai_secret():    
    return {"apikey": os.environ["OPENAI_API_KEY"]}