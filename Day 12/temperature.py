#low temp -> consistent, predictable
#high temp -> varied, creative

0.0 -1.2


import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise SystemExit("Set GROQ_API_KEY in a .env file first")

# Create Groq client
client = Groq(api_key=api_key)

# PROMPT
prompt = "Suggest a creative name for an AI tutoring app. Reply with just the name."
#once client obj that talks to the api
prompt = "Suggest a creative name for an ai tutoring app. Reply with just the name"
#TEMPERATURE
temperature = 0.8

# API Call
response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
)

# Get response
app_name = response.choices[0].message.content

# Print result
print("Suggested App Name:")
print(app_name)
