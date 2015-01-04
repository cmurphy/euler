from math import factorial

def find_permutations(nth, digits):
    num_perms = 0
    digits.sort
    string = ''
    for i in xrange(len(digits)):
        found = digits[i]
        # number of permutations total is factorial(len(digits))
        # number of permutations starting with a known digit is factorial(len(digits) - 1)
        # number of permutations after first i digits have been calculated is factorial(len(digits) - 1 - i)
        n = factorial(len(digits) - 1 - i)
        j = i
        while num_perms + n < nth:
            j += 1
            num_perms += n
            found = digits[j]
        digits.remove(found)
        digits.insert(0, found)
        string += str(found)
    return string

digits = range(0, 10) # 0 through 9
print find_permutations(1000000, digits)
