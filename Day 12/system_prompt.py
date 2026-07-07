"""
System prompts -- set the assistant's role and rules ONCE, up front.

The 'system' message is a special first turn that frames everything after it:
who the model is, how it should answer, what it must (not) do. Same user
question + different system prompt = very different answers.

Setup: pip install groq python-dotenv  (+ GROQ_API_KEY in .env)
Run:   python system_prompts.py
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


def ask(system_prompt, user_prompt):
    """One call: a system message + a user message -> the reply text."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0,          # deterministic, so the demo is stable
    )
    return response.choices[0].message.content.strip()


question = "What is recursion?"

# The SAME question, three different "personalities" set by the system prompt.
personas = {
    "Terse expert": "You are a terse expert. Answer in one sentence, no fluff.",
    "Kind tutor":   "You are a patient tutor for first-year students. Use a simple analogy.",
    "JSON only":    'You reply ONLY with JSON: {"term": ..., "definition": ...}. No prose.',
}

for name, system_prompt in personas.items():
    print(f"=== system = {name} ===")
    print(ask(system_prompt, question))
    print()

print("Same question, same model -- the system prompt changed the behaviour.")
print("Set the role/rules in the system message; keep the user message for the task.")