one = int(input())
two = int(input())
def roman():
    global one
    global two
    global three
    s_one = []
    three = one + two
    while one != 0:
        s_one.append(one % 10)
        one //= 10
    s_one = len(str(one))
    for i in range(s_one):
        pass


