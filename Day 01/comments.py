"""
Comments — notes for humans that Python ignores when running.

Run:
    python comments.py
"""

# This is a single-line comment. Python skips it entirely.

print("Comments don't affect output")  # <- this is an inline comment

# You can stack '#' lines to make a
# longer, multi-line explanation
# like this block.

# Good comments explain WHY, not the obvious WHAT:
total = 100
total = total - 10  # apply the flat ₹10 first-order discount

print("total after discount:", total)