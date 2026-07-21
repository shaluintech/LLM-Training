from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.graph.message import add_messages

class NoRrducer(TypedDict):
    log: list

def step_a(state): return{"log":["a ran"]}
def step_b(state):return{"log":["b ran"]}

b1 = StateGraph(NoRrducer)
b1.add_node("step_a",step_a)
b1.add_node("step_b",step_b)
b1.add_edge(START, "step_a")
b1.add_edge("step_a", "step_b")
b1.add_edge("step_b", END)
print(b1.compile().invoke({"log": []}))
print("  -> b's update REPLACED a's. History lost.\n")

class WithReducer(TypedDict):

    log: Annotated[list, add]

b2 = StateGraph(WithReducer)
b2.add_node("step_a", step_a)
b2.add_node("step_b", step_b)
b2.add_edge(START, "step_a")
b2.add_edge("step_a", "step_b")
b2.add_edge("step_b", END)
print(b2.compile().invoke({"log": []}))
print("  -> both kept. The reducer appended instead of replacing.\n")

class ChatState(TypedDict):
    messages: Annotated[list, add_messages]

def user_turn(state): return {"messages": [("human", "What's the capital of France?")]}
def bot_turn(state):  return {"messages": [("ai", "Paris.")]}

b3 = StateGraph(ChatState)
b3.add_node("user_turn", user_turn)
b3.add_node("bot_turn", bot_turn)
b3.add_edge(START, "user_turn")
b3.add_edge("user_turn", "bot_turn")
b3.add_edge("bot_turn", END)
msgs = b3.compile().invoke({"messages": []})
print("PART C (add_messages): history grew to", len(msgs), "messages")



