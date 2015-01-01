def d(n):
    sum = 0
    for x in xrange(1, n):
        if n % x == 0:
            sum += x
    return sum

def amicable_numbers(maxnum):
    table = ['-1'] # Pretend its 1-indexed
    amicables = []

    for x in xrange(1, maxnum):
        d_n = d(x)
        if len(table) > d_n and table[d_n] == x:
            amicables.append(x)
            amicables.append(d_n)
        table.append(d_n)

    sum = 0
    for x in amicables:
        sum += x

    return sum

print amicable_numbers(10000)
