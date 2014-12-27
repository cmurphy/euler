from math import sqrt

def divisible_triangle_num(num_sought_divisors):
    num_found_divisors = 0
    n = 1
    triangle = 0
    while num_found_divisors < num_sought_divisors:
        triangle += n
        print triangle
        n += 1
        tmp = 0
        max = int(sqrt(triangle))
        for i in xrange(1,max+1):
            if triangle % i == 0:  # Found a divisor
                if i == max:  # is sqrt
                    tmp += 1
                else:         # add 1 and n; 2 and n/2; etc
                    tmp += 2
            if tmp > num_found_divisors:
                num_found_divisors = tmp
        print "num found divisors: %d" % num_found_divisors
    return triangle

print divisible_triangle_num(500)
