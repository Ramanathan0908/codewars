from itertools import combinations

secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

def recoverSecret(triplets):
    rules = set()
    secret_set = set()
    for trip in triplets:
        for combi in combinations(trip, 2):
            rules.add(combi)
        for let in trip:
            secret_set.add(let)

    secret = [i for i in secret_set]
    alpha_order = dict.fromkeys(secret)
    for char in secret:
        alpha_order[char] = []
        for rule in rules:
            if char == rule[1]:
                alpha_order[char].append(rule[0])
    
    while True:
        swap_count = 0
        for i in range(0, len(secret)):
            for j in range(i + 1, len(secret)):
                if secret[j] in alpha_order[secret[i]]:
                    secret[i], secret[j] = secret[j], secret[i]
                    swap_count += 1
        if swap_count == 0:
            break

    return ''.join(secret)

print(recoverSecret(triplets))