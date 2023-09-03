m = int(input())
products = set()
for i in range(m):
    products.add(input())

n = int(input())
recipes = {}
for i in range(n):
    name_recipe = input()
    ingridients = set()
    k = int(input())
    for j in range(k):
        ingridients.add(input())
    recipes[name_recipe] = ingridients

results = []
for key in recipes:
    if recipes[key].issubset(products):
        results.append(key)

print("Можно приготовить", *results)