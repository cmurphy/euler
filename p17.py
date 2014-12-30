def numstrings():
    ones = [
      'one',
      'two',
      'three',
      'four',
      'five',
      'six',
      'seven',
      'eight',
      'nine'
    ]
    teens = [
      'ten',
      'eleven',
      'twelve',
      'thirteen',
      'fourteen',
      'fifteen',
      'sixteen',
      'seventeen',
      'eighteen',
      'nineteen'
      ]
    tens = [
      'twenty',
      'thirty',
      'forty',
      'fifty',
      'sixty',
      'seventy',
      'eighty',
      'ninety'
      ]
    hundreds = [
    ]

    numbers = ones + teens
    for ten in tens:
        numbers.append(ten)
        for one in ones:
            numbers.append(ten + one)
    for one in ones:
        hundreds.append(one + 'hundred')
    for hundred in hundreds:
        numbers.append(hundred)
        for x in xrange(99):
            numbers.append(hundred + 'and' + numbers[x])
    numbers.append('onethousand')

    return numbers

def sumstrings(strings):
    sum = 0
    for word in strings:
        sum += len(word)
    return sum

print sumstrings(numstrings())
