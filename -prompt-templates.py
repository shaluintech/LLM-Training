#pip install langchain langchain-groq python-dotenv
from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
load_dotenv()
MODEL = "llama-3.1-8b-instant"
prompt = ChatPromptTemplate.from_messages([("system", "You are a translator. Translate the text into {language}. Reply with only the translation."),
    ("human", "{text}"),

])
print("Templet variable needed", prompt.input_variables)
messages = prompt.format_messages(language="French", text="Good morning, friends!")

if not os.getenv("GROQ_API_KEY"):
    print("no api key")
else:
    Model = ChatGroq(model=MODEL, temperature=0)
    reply = Model.invoke(messages)              
    print("Model translation (French):", reply.content)
