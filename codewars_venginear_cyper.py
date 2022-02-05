from collections import deque

def encode_rail_fence_cipher(string, n):
    rails = [[] for i in range(n)]
    rail_index = 0
    rail_reverse = -1

    for char in string:
        rails[rail_index].append(char)
        if rail_index == n - 1 or rail_index == 0:
            rail_reverse = rail_reverse * -1
        rail_index = rail_index + rail_reverse

    return "".join("".join(arr for arr in rails[i]) for i in range(n))
    

def decode_rail_fence_cipher(string, n):
    if len(string) == 0:
        return ""
    if n == 1:
        return string
    result = [deque() for i in range(n)]
    inbetween_letter_count = 2*(n-2) + 1
    index = 0
    length = len(string)
    # First Rail
    while length > 0:
        result[0].append(string[index])
        index += 1
        length -= inbetween_letter_count
        length -= 1

    # Second Rail to second last rail
    inbetween_letter_count -= 2
    for i in range(1, n-1):
        length = len(string) - index
        while length > 0:
            if length >= inbetween_letter_count + 2:
                result[i].append(string[index])
                result[i].append(string[index+1])
                index += 2
                length -= inbetween_letter_count
                length -= 2
            else:
                result[i].append(string[index])
                index += 1
                break
        inbetween_letter_count -= 2

    # Last rail
    for i in range(index, len(string)):
        result[-1].append(string[i])

    # Converting rails to string
    result_str = ""
    rail_index = 0
    rail_reverse = -1

    while len(result_str) < len(string):
        result_str += result[rail_index].popleft()
        if rail_index == n - 1 or rail_index == 0:
            rail_reverse = rail_reverse * -1
        rail_index += rail_reverse

    return result_str


#print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3))
#print(len("oqjitcsgkcpzblnrssuhixtwryhle"))
print(decode_rail_fence_cipher("oqjitcsgkcpzblnrssuhixtwryhle", 7))
#print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3))