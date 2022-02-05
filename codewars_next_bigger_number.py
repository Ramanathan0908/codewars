from itertools import permutations

def next_bigger(n):
    """
    arr = [i for i in permutations(i for i in str(n))]
    arr = list(dict.fromkeys(arr))
    arr.sort()
    for i in range(len(arr)):
        if tuple(i for i in str(n)) == arr[i]:
            return int(''.join(arr[i + 1]))
    """
    """
    arr = [i for i in str(n)]
    #arr.sort()
    for i in permutations(arr):
        num = int(''.join(i))
        if num > n:
            print(num)
            break
    """
    arr = [int(i) for i in str(n)]
    arr2 = [i for i in arr]
    arr2.sort(reverse=True)
    if arr2 == arr:
        return -1
    arr.reverse()
    for i, digit in enumerate(arr):
        if digit > arr[i + 1]:
            arr3 = []
            for j in range(0, i + 1):
                if arr[j] > arr[i + 1]:
                    arr3.append(arr[j])
            min_digit = min(arr3)
            arr[arr.index(min_digit)] = arr[i + 1]
            arr[i + 1] = min_digit
            l = arr[:i + 1]
            l.sort(reverse=True)
            arr[:i + 1] = l
            break
    arr.reverse()
    arr4 = [str(i) for i in arr]

    return int(''.join(arr4))


print(next_bigger(5364))