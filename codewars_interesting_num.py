'''
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
'''

def is_interesting(num, awesome_phrases):
    if num < 98:
        return 0
    if num == 98 or num == 99:
        return 1
    for number in range(num, num + 3):
        str_num = str(number)
        power = len(str_num) - 1
        if number % (10 ** power) == 0:
            return 2 if number == num else 1

        incre = 0
        for i in range(0, len(str_num) - 1):
            if (int(str_num[i + 1]) - int(str_num[i])) == 1:
                incre += 1
            if int(str_num[i + 1]) == 0 and int(str_num[i]) == 9:
                incre += 1
        decre = 0
        for i in range(0, len(str_num) - 1):
            if (int(str_num[i + 1]) - int(str_num[i])) == -1:
                decre += 1

        if incre == len(str_num) - 1 or decre == len(str_num) - 1:
            return 2 if number == num else 1
        str_num2 = str_num[::-1]
        if str_num2 == str_num:
            return 2 if number == num else 1
        if number in awesome_phrases:
            return 2 if number == num else 1
    
    return 0