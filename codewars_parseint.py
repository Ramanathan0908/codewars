
def parse_int(string):
    units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 
        'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'ten']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    power_of_tens = ['', '', 'hundred', 'thousand', '', '', 'million']

    arr = [i for i in string.split() if i != 'and']
    arr.reverse()
    num = 0
    multiplier = 1
    last_multiple = 0
    for word in arr:
        if '-' in word:
            arr2 = word.split('-')
            num1 = tens.index(arr2[0]) * 10 + units.index(arr2[1])
            num += num1 * multiplier
        elif word in power_of_tens:
            if power_of_tens.index(word) > last_multiple:
                multiplier = 10 ** power_of_tens.index(word)
            elif power_of_tens.index(word) < last_multiple:
                multiplier *= 10 ** power_of_tens.index(word)
            last_multiple = power_of_tens.index(word)
        elif word in units or tens:
            num1 = units.index(word) if word in units else tens.index(word) * 10
            num += num1 * multiplier

    return num

print(parse_int('one'))
"""

words = {w: n for n, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
words.update({w: 10 * n for n, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
thousands = {w: 1000 ** n for n, w in enumerate('thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion'.split(), 1)}
def parse_int(strng):
    num = group = 0
    for w in strng.replace(' and ', ' ').replace('-', ' ').split():
        if w == 'hundred': group *= words[w]
        elif w in words: group += words[w]
        else:
            num += group * thousands[w]
            group = 0
    return num + group

print(parse_int('seven million'))
"""