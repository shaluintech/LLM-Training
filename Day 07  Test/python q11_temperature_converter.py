def convert(temp, to="C"):
    if to == "F":
        return round(temp * 9 / 5 + 32, 2)

    elif to == "C":
        return round((temp - 32) * 5 / 9, 2)

    else:
        return None
if __name__ == "__main__":
    print(convert(100,to="F"))
    print(convert(98.6))