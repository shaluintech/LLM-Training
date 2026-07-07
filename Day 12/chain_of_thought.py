"""
Chain-of-thought (CoT) prompting -- give the model room to REASON.

For multi-step problems (maths, logic, planning), asking for the answer
straight away invites mistakes. Telling the model to "think step by step"
first -- then state the answer -- dramatically improves accuracy.

The trade-off: you pay for the extra "thinking" tokens. Worth it for hard
reasoning; overkill for a simple lookup.

Setup: pip install groq python-dotenv  (+ GROQ_API_KEY in .env)
Run:   python chain_of_thought.py
"""

import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise SystemExit("Set GROQ_API_KEY in a .env file first (see the README).")

client = Groq(api_key=api_key)
MODEL = "llama-3.1-8b-instant"


def ask(system_prompt, question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()


problem = (
    "A shopkeeper has 3 cartons. Each carton holds 4 boxes. "
    "Each box holds 7 bulbs. He sells 15 bulbs. How many bulbs are left?"
)
# (3 * 4 * 7) - 15 = 84 - 15 = 69

# Force a bare answer -- no room to reason.
direct = "Answer with only a single number. No explanation."

# Invite reasoning first, then a clearly-marked final answer we can parse.
cot = (
    "Solve the problem. Think step by step and show your working. "
    "On the LAST line, write 'Answer: <number>' and nothing else after it."
)

print("=== Direct answer (no reasoning) ===")
print(ask(direct, problem))
print()

print("=== Chain-of-thought (reason, then answer) ===")
full = ask(cot, problem)
print(full)
print()

# In real code you'd parse just the final line after "Answer:".
final_line = [ln for ln in full.splitlines() if "answer" in ln.lower()]
print("Parsed final answer ->", final_line[-1].strip() if final_line else "(not found)")
print()
print("Lesson: 'think step by step' trades a few tokens for much better reasoning.")
print("Tip: ask for the answer in a fixed spot (last line) so code can extract it.")