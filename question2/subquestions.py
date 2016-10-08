import numpy as np
from migration import Landscape
import time

sequence_choices = range(25)

attempts = []
for s in range(25):
    for a in range(25):
        for b in range(25):
            for c in range(25):
                attempts.append([s, a, b, c])

print('Number of brute-force attempts to run:', len(attempts))
start = time.time()

correct_attempts = []

match = """1 0 1 0 0
1 0 1 0 0
1 0 0 0 0
1 0 1 0 0
1 0 0 0 0"""

for i, attempt in enumerate(attempts):
    if i % 10000 == 0:
        print('Attempt', i)
    landscape = Landscape(attempt[0], 8, attempt[1:])
    landscape.run_simulation()
    if match in str(landscape):
        print(attempt)
        correct_attempts.append(attempt)

print('Complete. Elapsed time:', time.time() - start)
print('Answer to 2c', len(correct_attempts))
