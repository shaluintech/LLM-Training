from pathlib import Path
SAMPLE = Path(__file__).resolve().parent / "hello.txt"
print(SAMPLE)
def read_whole_file() -> str:
    with open(SAMPLE, "r", encoding="utf-8") as f:
        return f.read()
print(read_whole_file())
def read_as_lines() -> list:
    with open(SAMPLE, "r", encoding="utf-8") as f:
        for number, line in enumerate(f,start=1):
            return f.readlines()
print(read_as_lines()) 

def write_to_file(text:str):
    with open(SAMPLE, "w", encoding="utf-8") as f:
        f.write(text)