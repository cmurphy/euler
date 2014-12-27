def is_divisible_by(x, divisors):
    for i in divisors:
        if x % i != 0:
#            print "%d is not divisible by %d" % (x, i)
            return False
    return True

def find_smallest_multiple(largest):
    mults = range(2,largest+1)
    i = 2
    while not is_divisible_by(i, mults):
        i += 1
        if i % 10000 == 0:
            print i
    return i

print find_smallest_multiple(20)
