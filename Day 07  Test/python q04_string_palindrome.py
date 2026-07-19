def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
if __name__ == "__main__":
    print(is_palindrome("Race car"))
    print(is_palindrome("hello"))