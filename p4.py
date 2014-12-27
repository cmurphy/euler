def is_palindrome(x):
    x_string = str(x)
    strlen = len(x_string)
    for i in xrange(strlen):
        if not (x_string[i] == x_string[strlen-i-1]):
            return False
    return True

def find_palindrome():
    x = 999

    cur = 0
    while x > 99:
        y = 999
        while y > 99:
            if is_palindrome(x*y):
                if x*y > cur:
                    cur = x*y
            y -= 1
        x -= 1
    return cur

print find_palindrome()
