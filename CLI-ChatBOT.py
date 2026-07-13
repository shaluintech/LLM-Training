from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Check API Key
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("❌ GROQ_API_KEY not found in .env file")

# Configuration
MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0

# Create LLM
llm = ChatGroq(
    model=MODEL_NAME,
    temperature=TEMPERATURE
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a helpful AI assistant.

        Rules:
        - Give clear and accurate answers.
        - Never repeat the same sentence.
        - If you don't know something, say "I don't know."
        - Keep your answers short unless the user asks for details.
        - Do not make up facts.
        """
    ),
    ("human", "{question}")
])

# Create Chain
chain = prompt | llm

print("=" * 50)
print("🤖 Welcome to CLI Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_input = input("\nYou: ").strip()

    # Exit
    if user_input.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    # Empty Input
    if not user_input:
        print("⚠️ Please enter a message.")
        continue

    try:
        response = chain.invoke(
            {
                "question": user_input
            }
        )

        print(f"\n🤖 Bot: {response.content}")

    except Exception as e:
        print(f"\n❌ Error: {e}")