import os
from typing import List

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import AIMessage
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.outputs import ChatResult, ChatGeneration
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()
MODEL = "llama-3.1-8b-instant"


@tool
def add(a: int, b: int) -> int:
    """Add two integers a and b and return the sum."""
    return a + b
if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model = ChatGroq(model=MODEL,temperature=0)
    agent = create_agent(model,[add],checkpointer=MemorySaver())
    config = {"configurable":{"thread_id":"Student-1"}}
    response1 = agent.invoke({"messages":[("human", "Hii my name is Shalu,,My age is 21,My full name is Shalu Gupta")]},config)
    print(response1['messages'][-1].content)
    response2 = agent.invoke({"messages":[("human", "What is my name")]},config)
    print(response2['messages'][-1].content)
    response3 = agent.invoke({"messages":[("human", "What is my age")]},config)
    print(response3['messages'][-1].content)
    response4 = agent.invoke({"messages":[("human", "What is my full name")]},config)
    print(response4['messages'][-1].content)
    
else:
    print("NO API KEY")