from pathlib import Path
import chromadb


BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / "chroma_store"
COLLECTION_NAME = "student_notes"


def main() -> None:
    client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = client.get_collection(COLLECTION_NAME)
    snapshot = collection.get(include=["documents", "metadatas"])

    # Print a small summary showing that the database reopened successfully.
    print("=" * 72)
    print("Reloaded Chroma collection from disk")
    print("=" * 72)
    print(f"Database folder : {DB_DIR}")
    print(f"Collection name : {COLLECTION_NAME}")
    print(f"Stored records  : {collection.count()}")

    print("\nSnapshot:")
    for doc_id, metadata, document in zip(
        snapshot["ids"],
        snapshot["metadatas"],
        snapshot["documents"],
    ):
        topic = metadata.get("topic", "unknown")
        print(f"- {doc_id} [{topic}] {document}")


if __name__ == "__main__":
    main()