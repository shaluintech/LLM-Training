def stats(*numbers):
    if len(numbers) == 0:
        return None

    total = 0
    smallest = numbers[0]
    largest = numbers[0]

    for num in numbers:
        total += num

        if num < smallest:
            smallest = num

        if num > largest:
            largest = num

    avg = total / len(numbers)

    return {
        "min": smallest,
        "max": largest,
        "avg": avg
    }
if __name__ == "__main__":
    print(stats(4, 8, 2, 6))  
    print(stats()) 
    