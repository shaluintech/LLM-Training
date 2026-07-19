from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
load_dotenv()

MODEL = "llama-3.1-8b-instant"
to_upper = RunnableLambda(lambda s : s.upper())
add_bang = RunnableLambda(lambda s : s + "!")
tiny_chain = to_upper| add_bang
print(tiny_chain.invoke("hello"))
prompt = ChatPromptTemplate.from_messages([
    "system", "you are a helpful assistant."
    "Answer in one short sentence"
    "human", "{question}"
])
parser = StrOutputParser()

if not os.getenv("GROQ_API_KEY"):
    print("no api key")
else:
    model=ChatGroq(model=MODEL)
    chain=prompt | model | parser
    answer=chain.invoke({"question": "what is python"})
    print(answer)
    answer2=chain.stream({"question": "whats are the newton's 3rd law oh motion"})
    for piece in answer2:
        print(piece,end="",flush=True)
    # 2b. batch: many inputs at once (runs them in parallel under the hood).
    questions = [
        {"question": "What is HTML?"},
        {"question": "What is HTTP?"},
    ]
    for q, a in zip(questions, chain.batch(questions)):
        print(f"batch -> {q['question']:12} {a}")
    print()