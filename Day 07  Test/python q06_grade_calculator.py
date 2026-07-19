def grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid"
    elif marks >= 90:
        return "A"
    elif marks >=75:
        return "B"
    elif marks >=60:
        return "c"
    elif marks >=50:
        return "D"
    else:
        return "F"
if __name__ == "__main__":
    print(grade (95))
    print(grade(65))
    print(grade(60))
    print(grade(50))
    print(grade(30))
    print(grade(101))