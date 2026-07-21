from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    text: str

def shout(state):
    return {"text": state["text"].upper() + "!"}

builder = StateGraph(State)
builder.add_node("shout", shout)
builder.add_edge(START, "shout")
builder.add_edge("shout", END)

graph = builder.compile()
result = graph.invoke({"text": "hello langgraph "})
print(result)