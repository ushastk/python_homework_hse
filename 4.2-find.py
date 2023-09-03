import random
import time
def MaxSearch(list):
    max_elem = list[0]
    elem = list[0]
    for elem in list:
        if max_elem < elem:
            max_elem = elem
    return max_elem

def MinSearch(list):
    min_elem = list[0]
    elem = list[0]
    for elem in list:
        if min_elem > elem:
            min_elem = elem
    return min_elem

def BinMaxSearch(list):
    list.sort()
    return list[-1]

def BinMinSearch(list):
    new_list = sorted(list)
    return new_list[0]


arrN = [100, 1000, 10000000]
dict_res = {}
for n in arrN:
    arr = [random.randint(1, 100) for _ in range(n)]
    t1 = time.time()
    BinMinSearch(arr)
    t2 = time.time()
    dict_res[n] = t2 - t1

print(dict_res)
# MaxSearch {100: 0.0, 1000: 0.0, 10000000: 0.2087078094482422}
# BinMaxSearch {100: 0.0, 1000: 0.0, 10000000: 0.8606553077697754}
# MinSearch {100: 0.0, 1000: 0.0, 10000000: 0.21986150741577148}
# BimMimSearch {100: 0.0, 1000: 7.224082946777344e-05, 10000000: 0.8885116577148438}
# линейный алгоритм показал себя лучше (даже на больших данных), но может это я в чем-то ошиблась. (на маленьких без разницы)