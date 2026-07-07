import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise SystemExit("Set GROQ_API_KEY in a .env file first")

#once client obj that talks to the api
client = Groq(api_key=api_key)

samples = [
    "hello",
    "I love learning about AI"
    "Antidistablishmentarianism"
    "namaste, kaise ho aap" #hindi in latin costs more tokens
    ]

def prompt_tokens(text):
    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [{"role":"user","content":text}]

    )
    return response.usage.prompt_tokens

for text in samples:
    print(f"{text}=> {prompt_tokens(text)}")