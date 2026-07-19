def averages(gradebook):
    result={}
    for grade,marks in gradebook.items():
        result=round(sum(marks)/len(marks), 2)
    return result

if __name__ == "__main__":
    book = {"Asha":[88,92,79], "ravi":[70,65,80], "meena": [95,99,91]}
    print(averages(book))
   

