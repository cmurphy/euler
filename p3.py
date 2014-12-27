from math import sqrt

def is_prime(x, known_primes):
    for i in known_primes:
        if x % i == 0:
            return False
    known_primes.append(x)
    return True

def factor(num):
    max = int(sqrt(num))
    known_primes = []
    cur = 1
    for x in xrange(2, max):
        if  num % x == 0 and is_prime(x, known_primes):
            cur = x
    return cur


print factor(600851475143)
