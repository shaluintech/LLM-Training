"""
05 - Runnables: branching and combining steps (beyond a straight line).

A chain isn't always a straight pipe. Sometimes you need to:
  * run several steps on the SAME input and collect the results  -> RunnableParallel
  * pass the input through UNCHANGED alongside a computed value   -> RunnablePassthrough
  * drop any plain function into the flow                         -> RunnableLambda

These three are the glue for real pipelines (including RAG). Best part: this
whole file runs OFFLINE - no key needed - because composition is pure Python.

Setup:
    pip install langchain
Run:
    python composition.py
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
word_count = RunnableLambda(lambda s: len(s.split()))
print("RunnableLambda word_count.invoke('one two three') =>", word_count.invoke("one two three"))
print()


analyze = RunnableParallel(
    upper=RunnableLambda(str.upper),
    words=RunnableLambda(lambda s: len(s.split())),
    chars=RunnableLambda(len),
)
print("RunnableParallel runs all branches on one input:")
print(" ", analyze.invoke("langchain is fun"))
print()

keep_and_shout=RunnableParallel(
    original=RunnablePassthrough(),
    shout=RunnableLambda(str.upper)
)
print("RunnablePassthrough")
print(keep_and_shout.invoke("hello"))

def fake_retriever(question:str)->str:
    return "Refund are processed within 5-7 business day to the original payment day"

prompt = ChatPromptTemplate.from_messages([
      ("system", "Answer ONLY from this context:\n{context}"),
    ("human", "{question}"),

])
rag_inputs = {
    "context": RunnableLambda(fake_retriever),   
    "question": RunnablePassthrough(),          
}
rag_prompt_chain = rag_inputs | prompt           

built = rag_prompt_chain.invoke("How long do refunds take?")
for m in built.to_messages():
     print(f"  [{m.type:>6}] {m.content}")
print()
