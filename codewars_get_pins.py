import itertools

def get_pins(observed):
    num_dict = {
        1: [1, 2, 4],
        2: [1, 2, 3, 5],
        3: [2, 3, 6],
        4: [1, 4, 5, 7],
        5: [2, 4, 5, 6, 8],
        6: [3, 5, 6, 9],
        7: [4, 7, 8],
        8: [5, 7, 8, 9, 0],
        9: [6, 8, 9],
        0: [0, 8]
    }
    arr = []
    for i in str(observed):
        arr.append(num_dict[int(i)])

    arr2 = []

    for tup in itertools.product(*arr):
        strn = ''
        for i in tup:
            strn += str(i)
        arr2.append(strn)

    return ','.join(arr2)

    
print(get_pins(11))