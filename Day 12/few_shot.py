"""
Few-shot prompting -- teach the task by SHOWING a few examples.

Instead of describing the rules in words, you give the model a handful of
(input -> output) examples. It copies the PATTERN: your exact labels, your
exact format. Great for niche categories and strict output shapes.

We supply examples as fake prior turns: example 'user' messages each followed
by the ideal 'assistant' reply. Then we send the real message last.

Setup: pip install groq python-dotenv  (+ GROQ_API_KEY in .env)
Run:   python few_shot.py
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

SYSTEM = "You route customer messages to a team. Reply with only the team name."

# The "shots": each example is a user message + the assistant's ideal answer.
# These teach the model our exact label set: ORDER / REFUND / DELIVERY / OTHER.
EXAMPLES = [
    ("Where is my package? It's 3 days late.", "DELIVERY"),
    ("I want my money back for the torn shirt.", "REFUND"),
    ("Can I change the size on order #4471?", "ORDER"),
    ("Do you have a store in Pune?", "OTHER"),
]


def build_messages(new_message, with_examples):
    messages = [{"role": "system", "content": SYSTEM}]
    if with_examples:
        for example_in, example_out in EXAMPLES:
            messages.append({"role": "user", "content": example_in})
            messages.append({"role": "assistant", "content": example_out})
    messages.append({"role": "user", "content": new_message})
    return messages


def route(new_message, with_examples):
    response = client.chat.completions.create(
        model=MODEL,
        messages=build_messages(new_message, with_examples),
        temperature=0,
    )
    return response.choices[0].message.content.strip()


tests = [
    "My order says delivered but I never got it.",
    "The blender I bought is faulty, I want a refund.",
    "Can I add one more item to order #9920?",
]

print("--- Zero-shot (no examples): labels may drift ---")
for message in tests:
    print(f"{route(message, with_examples=False):>20}  <-  {message}")

print()
print("--- Few-shot (4 examples): labels snap to ORDER/REFUND/DELIVERY/OTHER ---")
for message in tests:
    print(f"{route(message, with_examples=True):>20}  <-  {message}")

print()
print("Lesson: examples beat explanations for nailing format and edge cases.")