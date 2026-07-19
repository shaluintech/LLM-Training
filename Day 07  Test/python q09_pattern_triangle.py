def triangle(n):
    for r in range(1, n + 1):
        line = ""

        for _ in range(r):
            line += "* "

        print(line.rstrip())
if __name__ == "__main__":
    triangle(4)
