def is_pyth_triplet(a, b, c):
    if a < b and b < c:
        if a*a + b*b == c*c:
            return True
    return False

def find_triplet():
    a = 3
    b = 4
    c = 5
    for i in xrange(a, 1000):
        print i
        for j in xrange(b, 1000):
            for k in xrange(c, 1000):
                if i + j + k == 1000 and is_pyth_triplet(i, j, k):
                    return i, j, k

print find_triplet()
