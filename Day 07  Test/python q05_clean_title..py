def clean_title(messy):
    words = messy.split()

    result = []
    for word in words:
        result.append(word.capitalize())

    return " ".join(result)
if __name__ == "__main__":
    print (clean_title("hELLO wORLD"))
    print (clean_title("the TODO list"))