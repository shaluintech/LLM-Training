"""
Day 17 - Step 1: What is an embedding? (pure Python, NO libraries)

We pretend each word is described by just TWO made-up features:
    axis 1 = "how animal is it?"     axis 2 = "how vehicle is it?"
So every word becomes a point (x, y). Words with similar meaning sit close
together. We measure "close" with plain straight-line (Euclidean) distance.

This is embeddings in miniature: text -> numbers, and nearby = similar.
Real models (module 02) use hundreds of features picked by a trained model
instead of our 2 hand-made ones -- but the idea is exactly this.

Run:   python coordinates.py
"""

from math import sqrt
words = {
    "cat": (0.9, 0.1),
    "dog": (0.8, 0.2),
    "car": (0.1, 0.9),
    "truck": (0.2, 0.8),
}
def distance(a,b):
    """Straight-line distance between two points"""
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
def main():
    print("Each word is a point:\n")
    for word, vec in words.items():
        print(f"{word} = {vec}")

        #compare everything to 'cat' and sort from close to far

        target = "cat"
        scores = []
        for word, vec in words.items():
            if word == target:
                continue
            scores.append((word, distance(words[target], vec)))
        print(scores)

if __name__ == "__main__":
    main()

            #scores.sort(key=lambda pair:pair[1])
            #for word, dist in scores:
                #print(f"{target} <-> {word:6} = distance {dist:.2f}")