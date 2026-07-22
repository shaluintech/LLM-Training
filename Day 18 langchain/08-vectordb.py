from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

docs = [
    Document(page_content="Refunds are processed within 5 business days to the original payment method.",
             metadata={"source": "refunds"}),
    Document(page_content="We ship across India; standard delivery takes 4 to 7 working days.",
             metadata={"source": "shipping"}),
    Document(page_content="Reach support at help@example.in or 1800-123-456, 9am to 6pm.",
             metadata={"source": "support"}),
    Document(page_content="Cash on delivery is available for orders under 5000 rupees.",
             metadata={"source": "payment"}),
]

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

store = Chroma.from_documents(docs, embedding=embeddings)
print(f"Indexed {len(docs)} documents in an in-memory Chroma store.\n")


query = "how do I get my money back?"
results = store.similarity_search(query, k=2)
print(f"similarity_search({query!r}, k=2):")
for d in results:
    print(f"  [{d.metadata['source']:8}] {d.page_content}")
print()

print("with scores (lower distance = closer):")
for d, score in store.similarity_search_with_score(query, k=2):
    print(f"  {score:.3f}  [{d.metadata['source']}]")
print()

retriever = store.as_retriever(search_kwargs={"k": 2})
results3 = retriever.invoke("when will my order arrive?")
print("retriever.invoke('when will my order arrive?'):")
for d in results:
    print(f"  [{d.metadata['source']:8}] {d.page_content}")
print()

print("Takeaway: Documents + local embeddings -> Chroma -> .as_retriever().")
print("A retriever is just a Runnable that returns Documents -- RAG's 'R'.")
print("Next: pipe it into a prompt|model|parser chain to get grounded answers.")