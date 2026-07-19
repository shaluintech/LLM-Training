
import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_tool

load_dotenv()
MODEL = "llama-3.1-8b-instant"

def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the exact result."""
    return a * b


@tool
def word_count(text: str) -> int:
    """Count how many words are in a piece of text."""
    return len(text.split())


TOOLS = [multiply, word_count]

questions = [
    "What is 24 * 7?",             
    "How many words in 'the quick brown fox jumps'?",  
    "Say hello in one word.",      
]
from langchain_groq import ChatGroq
llm = ChatGroq(model=MODEL, temperature=0)
llm_with_tools = llm.bind_tools(TOOLS)
for q in questions:
     print("=" * 60)
     print(f"Q: {q}")
     resp = llm_with_tools.invoke(q)
     print(resp)
     if resp.tool_calls:
         for call in resp.tool_calls:
             print(f"Model wants tool:{call['name']} args   {call['args']}")
             print("  (content is empty -- the model is waiting for the tool result)")
     else:
        
        print(f"  no tool needed. answer: {resp.content}")
