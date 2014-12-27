def fib(final):
    last = 0
    curr = 1
    while last < final:
        tmp = curr
        curr = curr + last
        last = tmp
        yield last

def sum_evens_of_fib(final):
    sum = 0
    for i in fib(final):
        if i % 2 == 0:
            sum += i
    return sum

print sum_evens_of_fib(4000000)
