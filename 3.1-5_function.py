def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
print(distance(3, 0, 0, 4))

def reverse_list(lst):
    new_lst = []
    for i in range(len(lst)-1, -1, -1):
        new_lst.append(lst[i])
    return new_lst
print(reverse_list([8, 1, 0, 4]))


#def reverse_even(x):
 #   odd = []
#    even = []
#   new_x = []
#   for i in range(len(x)):
#       if i % 2 != 0:
 #           odd.append(x[i])
 #       else:
 #           even.append(x[i])
#    sorted(odd, reverse=True)
#    for i in range(len(odd)+ len(even)):
 #       if i % 2 == 0:
 #           new_x.append(even[i])
 #       else:
 #           new_x.append([odd[i]-1])
#
#    return new_x

# print(reverse_even([0, 1, 2, 3,4, 5, 6, 7, 8, 9]))


def number():
    for i in range(501):
        if '8' in str(i) and i % 7 == 0:
            print(i, end=" ")
print(number())


def more_than_five(lst):
    new_lst = []
    for elem in lst:
        if abs(elem) > 10:
            new_lst.append(elem)
    return new_lst
print(more_than_five([1, 10, 40, -500, 3, 2]))


