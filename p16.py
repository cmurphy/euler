def sum_digits(n):
    sum = 0
    nstr = str(n)
    for i in nstr:
        sum += int(i)
    return sum

print sum_digits(2**1000)
