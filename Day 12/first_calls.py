import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise SystemExit("Set GROQ_API_KEY in a .env file first")

#once client obj that talks to the api
client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model = "llama-3.1-8b-instant",
    messages = [
        {"role":"system", "content":"your are a lyrics writter for bollywood songs who answers everything in song lyrics in"},
        {"role": "user", "content":"Explain what is full stack development"}
        ]
    )

print("Model's Response")
print(response.choices[0].message.content)