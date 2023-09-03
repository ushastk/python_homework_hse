from sys import stdin
print("Когда закончите вводить таблицу введите cntrl+D")
lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))

textbooks_titles = [i for i in lines[0].lstrip().split("\t")]
#print(textbooks_titles)

name_of_shop_price = {}
for i in range(1, len(lines)):
    s = lines[i]
    s_name_of_shop = s.split("\t")
    s_price = s.split()
    name_of_shop_price[s_name_of_shop[0]] = [ int(i) for i in s_price[-len(textbooks_titles):]]
#print(name_of_shop_price)
min_price = min(name_of_shop_price.items(), key=lambda x: sum(x[1]))
#print(min_price)
print(min_price[0])
for shop, price in zip(textbooks_titles, min_price[1]):
    print(f'{shop}      {price}')