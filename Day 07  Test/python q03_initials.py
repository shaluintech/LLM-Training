def initial(full_name):
    words = full_name.split()
    result = ""
    for word in words:
        result += word[0].upper() + "."
    return result
if __name__ == "__main__":
    print(initial("Tushar ravi rohan"))
    print(initial("tushar verma"))


