from math import factorial

def sum_factorial(n):
    number = str(factorial(n))
    sum = 0
    for c in number:
        sum += int(c)

    return sum

print sum_factorial(100)
