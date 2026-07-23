import os
from typing import List
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import AIMessage
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.outputs import ChatResult,ChatGeneration

load_dotenv()
MODEL="llama-3.1-8b-instant"
@tool
def multiply(a:int,b:int)->int:
    """MUltiply two integers a and b and return the product"""
    return a*b
@tool
def add(a:int,b:int)->int:
    """Add two integers and return the sum""" 
    return a+b  
TOOLS=[ add,multiply]
if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model = ChatGroq(model=MODEL,temperature=0)
    agent = create_agent(model, TOOLS)
    question = "Add 34 with 13 and then add 150 to it's result"
    #result = agent.invoke({"messages":[("human",question)]})
    
    #print(result)
    for chunk in agent.stream({"messages":[("human",question)]}):
        for node , update in chunk.items():
            last = update["messages"][-1]
            if getattr(last,"tool_calls",None):
                    c= last.tool_calls[0]
                    print(f"[{"node"}] REASON + ACT ->call{c['name']} (c['args])")
            elif type(last).__name__ == "ToolMessage":
                print(f"  [{node:5}] OBSERVE     -> tool returned {last.content!r}")
            elif last.content:
                print(f"  [{node:5}] ANSWER      -> {last.content!r}")

else:
    print("No API Key")

