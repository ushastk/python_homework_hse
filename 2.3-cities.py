import itertools
from sys import stdin

print("Введите cntrl+D, чтобы закончить ввод.")
cities = []
for line in stdin:
    cities.append(line.rstrip('\n').split())

for elem in cities:
    elem[2] = int(elem[2]) - int(elem[2]) % -100000

cities.sort(key=lambda x: x[2])

sort_cities = []
population = []
for pop, city in itertools.groupby(cities, key=lambda x: x[2]):
    population.append(pop)
    sort_cities.append(list(city))

new_cities = []
for i in range(len(sort_cities)):
    new_cities.append([])
    for j in range(len(sort_cities[i])):
        s = sort_cities[i][j][0]
        new_cities[i].append(s)

for pop, capital in zip(population, new_cities):
    print(pop//1000-100, "-", str(pop//1000) + ":",end=' ')
    print(*capital, sep=', ')

#round_func = lambda x: (x[2] - x[2] % int(-100000))- 100000 < x[2] <(x[2] - x[2] % -100000)  # округление и получение диапазона
