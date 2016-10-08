## Copyright (c) 2016 Mikel Bober-Irizar
# British Informatics Olympiad 2016
# Question 3 - Prime Connections

from primeconnector import PrimeConnector

# Question 3b solution
pc = PrimeConnector(20, max_depth=15, debug=True)
print('Question 3b answer:', pc.tree_path_search(2, 19))

# Question 3c solution
pc = PrimeConnector(250000)
print('Question 3c answer:', pc.find_connected_pairs())
