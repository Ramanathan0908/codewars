"""
permutational_primes(1000, 3) ==> [3, 149, 379]
''' 3 primes with 3 permutations below 1000, smallest: 149, largest: 379 '''

permutational_primes(1000, 2) ==> [9, 113, 389]
''' 9 primes with 2 permutations below 1000, smallest: 113, largest: 389 '''

permutational_primes(1000, 1) ==> [34, 13, 797]
''' 34 primes with 1 permutation below 1000, smallest: 13, largest: 797 '''
"""
from itertools import permutations

def sieve_of_eratosthenes(n):
	primes = [True for i in range(n)]

	for i in range(2, int(n ** 0.5) + 1):
		if not primes[i]:
			continue
		else:
			for j in range(i * i, n, i):
				primes[j] = False

	#return [str(i) for i, value in enumerate(primes) if value and i > 2]
	return primes

'''
def permutational_primes(upper_limit, n):
	print(upper_limit)
	primes = sieve_of_eratosthenes(upper_limit)
	permu_primes = []
	no_go = []
	for prime in primes:
		tmp = set()
		for i in permutations(prime, len(prime)):
			j = ''.join(i)
			if j in primes and j not in no_go:
				tmp.add(j)
				no_go.append(j)
		if len(tmp) == n + 1:
			permu_primes.append(prime)
	if len(permu_primes) == 0:
		return [0, 0, 0]
	sol = [len(permu_primes), int(permu_primes[0]), int(permu_primes[-1])]
	return sol
'''
def permutational_primes(upper_limit, n):
	primes = sieve_of_eratosthenes(upper_limit)
	permu_primes = []
	for i, prime in enumerate(primes):
		if not prime:
			continue
		else:
			count = 0
			for j in permutations(str(i), len(str(i))):
				if ''.join(j)[0] != '0':
					z = int(''.join(j))
					if z < upper_limit:
						if primes[z]:
							primes[z] = False
							count += 1
			if count == n + 1:
				permu_primes.append(i)
	if len(permu_primes) == 0:
		return [0, 0, 0]
	#print(permu_primes)
	#return [len(permu_primes), permu_primes[0], permu_primes[-1]]
	return permu_primes

def debug(permu, limit, n):
	primes = sieve_of_eratosthenes(limit)
	new = []
	for prime in permu:
		tmp = []
		for i in permutations(str(prime), len(str(prime))):
			j = ''.join(i)
			if j[0] != '0':
				if int(j) < limit:
					if primes[int(j)] and int(j) not in tmp:
						tmp.append(int(j))
						new.append(int(j))
						print(int(j))
		print()
	print(len(new))
	for num in new:
		if not primes[num]:
			print('no')
					

#print(permutational_primes(46091, 2))
print(debug(permutational_primes(15299, 1), 15299, 1))
