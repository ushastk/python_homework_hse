l = [int(elem) for elem in input().split()]
my_list = [0] * (len(l) + 2)

for i in range(1, len(l)+1):
    my_list[0] = ["*"] * (max(l) + 2)
    my_list[len(l) + 1] = ["*"] * (max(l) + 2)
    my_list[i] = [" "] * (max(l) + 2) # высота столбика
    my_list[i][(max(l)+2)-l[i-1]:] = "*" * l[i-1]  # ширина диаграммы
    my_list[i][0] = "*"

for k in range(max(l)+2):
    for j in range(len(l)+2):
        print(my_list[j][k], end="")
    print()