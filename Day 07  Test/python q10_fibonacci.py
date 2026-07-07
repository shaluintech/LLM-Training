def fibonacci(count):
    a, b = 0, 1
    seq = []

    for _ in range(count):
        seq.append(a)
        a, b = b, a + b

    return seq
if __name__ == "__main__":
    print(fibonacci(10))
    print(fibonacci(1))

