def is_prime(x, known_primes):
    for i in known_primes:
        if x % i == 0:
            return False
    known_primes.append(x)
    return True

def primes(nth):
    known_primes = []
    n = 2
    i = 1
    while i <= nth:
      if is_prime(n, known_primes):
          i += 1
      n += 1
    return known_primes

print primes(10001)
