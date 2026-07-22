#pip install langchain
#pip install langchain groq
#pip install python-dotenv
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

load_dotenv()

MODEL = "llama-3.1-8b-instant"
messages = [SystemMessage("You are a concise assistant .Answer in one sentence."),
           HumanMessage("Explain what  an API is "),]
print("The messages we will send (role->text):")
for m in messages:
    print(f"  [{m.type:>6}] {m.content}")
    
print()

if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY set -skipping the live call (this is fine).")
    print("Add a key to .env to see the real answer")

else:
    model = ChatGroq(model=MODEL, temperature=0)
    reply = model.invoke(messages)

    print("Reply type:", type(reply).__name__)   # AIMessage
    print("Answer    :", reply.content)
    usage = reply.usage_metadata
    if usage:
        print("Tokens    :", usage)   
print()
print("Why bother with the wrapper? To switch providers you change ONE line:")
print('  Groq    :  model = ChatGroq(model="llama-3.1-8b-instant")')
print('  OpenAI  :  model = ChatOpenAI(model="gpt-4o-mini")')
print('  Ollama  :  model = ChatOllama(model="llama3.1") ') # 100% local'
print("Everything built on top -- prompts, chains, parsers, memory -- stays the same.")
