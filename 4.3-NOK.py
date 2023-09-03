import random # как время выполнения программа посчитать
import time
def lcm(a, b):
    import math
    return (a * b) // math.gcd(a, b)

def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def evklid_lcm(a, b):
    return (a * b) // gcd(a, b)


num1 = random.randint(1000, 100000)
num2 = random.randint(1000, 100000)
print(num1, num2)
t1 = time.time()
calculate_lcm(num1, num2)
t2 = time.time()
res = t2 - t1

print(res)
