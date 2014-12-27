def sum(x):
    total = 0
    for i in xrange(x):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print sum(1000)
