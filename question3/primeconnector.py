## Copyright (c) 2016 Mikel Bober-Irizar
# British Informatics Olympiad 2016
# Question 3 - Prime Connections

import numpy as np

class PrimeConnector():
    # max_prime: The upper bound of the prime numbers allowed
    # max_depth: Maximum depth of the search tree
    def __init__(self, max_prime, max_depth=12, debug=False):
        self.max = max_prime
        self.debug = debug
        self.max_depth = max_depth

        # Generate static arrays of primes and powers of two and keep in memory to speed up computation.
        self.primes = set(self.gen_primes(self.max))
        self.powers = self.gen_powers(self.max)

    # Super fast prime number sieve - http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
    def gen_primes(self, n):
        sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
        for i in range(1, int(n ** 0.5) // 3 + 1):
            if sieve[i]:
                k = 3 * i + 1 | 1
                sieve[k * k // 3::2 * k] = False
                sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
        return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]

    # Generate powers of two
    def gen_powers(self, n):
        powers = []
        i = 1
        while i < n:
            powers.append(i)
            i *= 2
        return np.array(powers)

    # Given a prime number, p, find all other primes with a 2^n distance.
    def find_leaves(self, p):
        plus = self.powers + p
        minus = self.powers - p
        plus_intersect = self.primes.intersection(plus)
        minus_intersect = self.primes.intersection(minus)
        leaves = list(plus_intersect) + list(minus_intersect)
        return leaves

    # Performs a tree search to find the shortest connection route between two prime numbers.
    # Returns the minimum number of nodes needed to connect the prime numbers.
    def tree_depth_search(self, p, q):
        solved = 0
        old_leaves = [p]
        depth = 2
        while solved == 0:
            depth += 1
            if depth > self.max_depth:
                print('Reached maximum search depth without solution.')
                depth = np.nan
                break
            if self.debug:
                print('Computing depth', depth, 'leaf count', len(old_leaves))
            new_leaves = []
            for l in old_leaves:
                leaves = self.find_leaves(l)
                if q in leaves:
                    solved = 1
                    break
                new_leaves.extend(leaves)
            old_leaves = new_leaves
        return depth

    # Finds the number of possible paths between two prime numbers
    def tree_path_search(self, p, q):
        solutions = 0
        old_leaves = [p]
        depth = 0
        while depth < self.max_depth:
            depth += 1
            if self.debug:
                print('Computing depth', depth, 'leaf count', len(old_leaves), 'path count', solutions)
            new_leaves = []
            for l in old_leaves:
                leaves = self.find_leaves(l)
                for l2 in leaves:
                    if l2 == p:
                        solutions += 1
                    else:
                        new_leaves.append(l2)
            if len(new_leaves) == 0:
                if self.debug:
                    print('Proven solution found.')
                return solutions
            old_leaves = new_leaves
        print('Maximum depth reached without proven solution. Halting.')
        return solutions

    # Finds the number of possible prime connections that could be made
    def find_connected_pairs(self):
        connections = 0
        for prime in self.primes:
            connections += len(self.find_leaves(prime))
        return connections / 2

# Question 3a solution
if __name__ == "__main__":
    max_prime, p, q = [int(i) for i in input().split(' ')]
    pc = PrimeConnector(max_prime)
    print(pc.tree_depth_search(p, q))
