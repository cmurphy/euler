def fib():
    f1 = 1
    f2 = 1
    while True:
        yield f1
        tmp = f2
        f2 = f2 + f1
        f1 = tmp

def digits(x):
    x_str = str(x)
    return len(x_str)

i = 0
for x in fib():
    i += 1
    if digits(x) >= 1000:
        print i
        break
