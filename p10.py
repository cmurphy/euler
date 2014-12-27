def is_prime(x, known_primes):
    for i in known_primes:
        if x % i == 0:
            return False
    known_primes.append(x)
    return True

def sum_primes(nth):
    known_primes = []
    n = 2
    sum = 0
    while n <= nth:
      if n % 1000 == 0:
          print n
      if is_prime(n, known_primes):
          sum += n
      n += 1
    return sum

print sum_primes(2000000)
