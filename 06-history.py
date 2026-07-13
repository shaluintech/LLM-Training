from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq

load_dotenv()
MODEL="llama-3.1-8b-instant"

prompt=ChatPromptTemplate.from_messages([
    ("system","You are a friendly assistant. Keep answers to one line."),
    MessagesPlaceholder("history"),
    ("human", "{input}"),
])

def run_conversation(model, label):
    chain = prompt | model | StrOutputParser()
    history =[]
    
    for user_text in ["Hi! My name is Riya.", "What is my name?"]:
        answer=chain.invoke({"history":history,"input":user_text})
        history.append(HumanMessage(user_text))
        history.append(AIMessage(answer))
        
        print(f"You: {user_text}")
        print(f"Bot: {answer}")
    print(f"(history now holds {len(history)} messages)")
    print()


def fake_llm(prompt_value):
    msgs = prompt_value.to_messages()
    humans = [m.content for m in msgs if m.type == "human"]
    return AIMessage(
        content=f"(I was given {len(msgs)} messages; humans so far: {humans})"
    )

print("OFFLINE demo - watch the message count grow as history is remembered:\n")
run_conversation(RunnableLambda(fake_llm), "offline-fake-model")

if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY")
    print("No API key available")
else:
    chat_model= ChatGroq(model=MODEL)
    run_conversation(chat_model, "Live chat")

print("This is Day 16's 'append every turn', now wired through a prompt placeholder.")
print("For heavier state (branching, tools, long-term memory) Phase 3 moves to LangGraph,")
print("which stores and re-injects this history for you automatically.")