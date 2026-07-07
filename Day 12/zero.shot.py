"""
Zero-shot prompting -- ask directly, with NO examples.

"Zero-shot" = you give instructions only and trust the model to figure it out.
It works well when the task is common and your instructions are CRISP:
say exactly what to do, the allowed outputs, and the format.

Setup: pip install groq python-dotenv  (+ GROQ_API_KEY in .env)
Run:   python zero_shot.py
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


def classify(review, instruction):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": review},
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()


# Product reviews (think of a Rs. 1,299 pair of earphones on an e-commerce site).
reviews = [
    "Battery lasts two days and the bass is amazing. Totally worth it!",
    "Stopped working in a week. Waste of money.",
    "It's okay. Does the job but nothing special.",
]

# A VAGUE instruction -- the model may ramble or invent its own labels.
vague = "Tell me about this review."

# A CRISP zero-shot instruction -- one allowed label, fixed format, no extra words.
crisp = (
    "Classify the customer review's sentiment. "
    "Reply with exactly one word: Positive, Negative, or Neutral. No other text."
)

print("--- Vague instruction (unpredictable) ---")
print(classify(reviews[0], vague))
print()

print("--- Crisp zero-shot instruction (clean labels) ---")
for review in reviews:
    print(f"{classify(review, crisp):>8}  <-  {review}")

print()
print("Lesson: zero-shot works when you state the task, the allowed answers,")
print("and the exact format. Vague in -> vague out.")