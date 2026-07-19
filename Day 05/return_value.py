"""
return - send value back so that it can be used
"""

def add(a,b):
    return a+b


total = add(4,5)
print(add(9,10))
print(total)


def safe_divide(a,b):
    if b == 0:
        return "Cannot divide by 0"
    return a/b 

# Functions can also return multiple values 
#python puts them in a tuple

def min_max_avg(numbers):
    return min(numbers), max(numbers),sum(numbers)/len(numbers)

scores = [65,32,76,90,54]
print(min_max_avg(scores))
low , high , avg = min_max_avg(scores)
print(f"Lowest: {low}, Highest : {high}, Avg :{avg}")