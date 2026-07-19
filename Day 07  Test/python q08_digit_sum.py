def digit_sum(n):
    if n  == 0:
        return (0, 1)

total = 0 
count = 0
while n > 0:
    total += n % 10
    n = n // 10
    count += 1
return (total, count)
print(digit_sum(4096))
print(digit_sum(0))




 
