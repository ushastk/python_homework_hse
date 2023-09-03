vessels = [set()]
s = input()
vessels[len(vessels)-1].add(s)
while s != "":
    s = input()
    vessels[len(vessels)-1].add(s)
    if s == '-1':
        vessels.append(set())
del vessels[len(vessels)-1]
for i in range(len(vessels)):
    vessels[i].remove('-1')


res = {}
for v in vessels:
    for v_i in v:
        num_count = res.get(v_i)
        if num_count:
            res[v_i] = num_count + 1
        else:
            res[v_i] = 1
for v_i in res.keys():
    if res[v_i] == 1:
        print(v_i, end=' ')
