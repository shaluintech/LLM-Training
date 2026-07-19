

def  square_def(n):
    """This function returns the square of a number"""
    return n*n

square_lambda = lambda n:n*n
print(square_def(10))
print(square_lambda(10))

add = lambda a,b: a+b


nums = [1,2,3,4,5,6]
#map : apply a function to every item
double = list(map(lambda n:n*2,nums))
print(double)

nums = [1,2,3,4,5,6]
#map : apply a function to every item
double = list(map(lambda n:n**2,nums))
print(double)

test = map(lambda n:n*2,nums)
print(test)

evens = list(filter(lambda n: n%2==0,nums))
print(evens)