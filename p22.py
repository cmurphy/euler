def alpha_value(c):
    return ord(c.lower()) - ord('a') + 1

def names_scores(file):
    f = open(file, 'r')
    names = f.read().replace('"', '').split(',')
    names.sort()
    sum = 0
    for i in xrange(len(names)):
        score = 0
        for c in names[i]:
            score += alpha_value(c)
        score *= i + 1
        sum += score
    return sum

print names_scores('p22.txt')
