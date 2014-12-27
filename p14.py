def is_even(n):
    return n % 2 == 0

def when_even(n):
    return n/2

def when_odd(n):
    return 3*n + 1

def collatz(n):
    chain = [n]
    while n != 1:
        if is_even(n):
            n = when_even(n)
        else:
            n = when_odd(n)
        chain.append(n)
    return chain

def find_longest(max_start):
    longest = 0
    longest_start = 0
    for i in xrange(1, max_start+1):
        if i % 1000 == 0:
            print i
        chain = collatz(i)
        if len(chain) > longest:
            longest = len(chain)
            longest_start = i
    return longest_start

print find_longest(1000000)
