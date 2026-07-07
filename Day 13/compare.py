from sentence_transformers import SentenceTransformer,util
DOCS =[
    "A car is a four wheeled vehicle for the road",
    "An automobile takes you from one place",
    "The chef cooked a delicious pasta dinner",
    "Photosyntesis lets plants make food from light",
]

QUERY = "How does a motor vehicle work?"
def main():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_vec = model.encode(QUERY)
    doc_vecs = model.encode(DOCS)
    scores = util.cos_sim(query_vec, doc_vecs)[0]
    print(scores)

if __name__ == "__main__":
    main()