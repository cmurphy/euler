from decimal import *

MAX_DENOMINATOR = 1000
MAX_FRACTION_LENGTH = 20000

def check_next_sequence(fraction, index, length):
    return fraction[index:index+length] == fraction[index+length:index+2*length]

def done_processing(fraction, index, length):
    if len(fraction) < index + 2*length:
        return True
    return False

def find_pattern(fraction):
    pattern = None
    max_pattern_length = MAX_FRACTION_LENGTH/2
    for length in range(1, max_pattern_length + 1):
        for i in range(len(fraction)-length):
            found = False
            done = False
            current = i
            while not done:
                done = done_processing(fraction, current, length)
                if done:
                    break
                found = check_next_sequence(fraction, current, length)
                if not found:
                    break
                else:
                    current += length
                if current > len(fraction):
                    break
            if found:
                pattern = fraction[i:i+length]
                break
        if pattern:
             return pattern
    return pattern

def main():
    getcontext().prec = MAX_FRACTION_LENGTH
    getcontext().flags.clear()
    patterns = {}
    for d in range(2,MAX_DENOMINATOR):
        print d
        fraction = Decimal(1) / Decimal(d)
        if getcontext().flags and getcontext().flags[Inexact]:
            fraction = str(fraction).split('.')[1][:-1] # chop off rounding digit
            pattern = find_pattern(str(fraction))
            if pattern:
                patterns[d] = pattern
    longest_pattern = max(patterns, key=lambda k: len(patterns[k]))
    print patterns
    print longest_pattern
    print patterns[longest_pattern]

main()
