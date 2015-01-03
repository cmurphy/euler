# This is sort of brute-force with some optimizations by
# eliminating some possibilities ahead of time.
# Should probably refine this later.
# real time: 13m23.965s :(

def proper_divisors(n):
    divisors = [1]
    for i in xrange(2, n/2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_abundant(n):
    divisors = proper_divisors(n)
    sum = 0
    for i in divisors:
        sum += i
    if sum > n:
        return True
    return False

def find_non_abundant_sums(possibilities, abundants, max):
    sum = 0
    for i in possibilities:
        found_sum = False
        for j in abundants:
            # j + something in abundants == i means this is the sum of two abundants
            if j > i/2:
                break
            if i - j in abundants:
                found_sum = True
                break
        if found_sum == False:
            sum += i
    return sum

def find_abundant_numbers(max):
    abundants = []
    for i in xrange(1, max+1):
        if is_abundant(i):
            abundants.append(i)
    return abundants

def remove_abundant_multiples(possibilities, abundants, max):
    for i in abundants:
        for j in xrange(2, max/i+1):
            if i * j in possibilities:
                possibilities.remove(i*j)
    return possibilities

def main():
    max = 28123
    print "finding possibilities"
    possibilities = range(1, max+1)
    print "finding abundants"
    abundants = find_abundant_numbers(max)
    print "refining abundants"
    possibilities = remove_abundant_multiples(possibilities, abundants, max)
    print "summing non abundant sums"
    print find_non_abundant_sums(possibilities, abundants, max)

main()
