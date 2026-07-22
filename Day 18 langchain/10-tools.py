from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return exact result."""
    return a * b

@tool
def word_count(text: str) -> int:
    """Count how many words are there in text."""
    return len(text.split())

print("What the model sees about each tool")
print("=" * 60)

for t in (multiply, word_count):
    print(f"Name        : {t.name}")
    print(f"Description : {t.description}")
    print(f"Args        : {t.args}")
    print("-" * 60)

print(multiply.invoke({"a": 6, "b": 7}))
print(word_count.invoke({"text": "tools let models act"}))