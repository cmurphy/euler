def sum_squares(n):
    sum = 0
    for i in xrange(n+1):
        sum += i*i
    return sum

def square_sum(n):
    sum = 0
    for i in xrange(n+1):
        sum += i
    return sum*sum

print square_sum(100)- sum_squares(100)
