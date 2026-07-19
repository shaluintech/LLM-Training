#pip install sentence-transformers numpy
from sentence_transformers import SentenceTransformer
def main():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    sentences = "I Love AI"
    vector = model.encode(sentences)
    print(vector)

    sentences =[
        "This cat sat on the mat.",
        "The feline restued on the rug.",
        "Interest rates rose this quarter."
    ]
    vectors = model.encode(sentences)
    print(vectors)
if __name__ == "__main__":
    main()