import itertools
from itertools import product
suits = ["бубен", "червей", "пик", "треф"]
s = input()
suits.remove(s)
denominations = [i for i in range(2, 11)] + [ "валет", "дама", "король", "туз"]
for d, s in itertools.product(denominations, suits):
    print(d, s)