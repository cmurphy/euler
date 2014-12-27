from math import factorial

def nCr(n,r):
    numer = factorial(n)
    denom = factorial(r) * factorial(n - r)
    return numer / denom

print nCr (2 * 20, 20)
