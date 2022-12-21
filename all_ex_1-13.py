
# 1
result = []
for i in range(1000):
    if i % 17 == 0:
        result.append(i)

print(result)



# 2
result = []
for i in range(1000):
    a = str(i)
    if '2' in a:
        result.append(i)
        
print(result)


# 3
result = []
for i in range(10000):
    if str(i) == str(i)[::-1]:
        result.append(i)
        
print(result)
    
    
    
# 4
line = input()
if " " in line:
    result = line.count(' ')
    print(result)
else:
    print('ошибка')
    
    
    
    
# 5
vowels = ["a", "e", "i", "o", "u", "y"]
input_str = "HelloEarth"
result = []
for c in input_str:
    if c.lower() not in vowels:
        result.append(c)
result_str = "".join(result)
print(result_str)



# 6
string = input()
result = [i for i in string.split() if len(i) <= 5]
print(result)



# 7
string = input()
line = string.split()
result = {i: len(str(i)) for i in line}

print(result)



# 8
element = ['a', 'd', 'f', 's', 'd', 'g', 'f', 'd', 'f', 's', 's']
def get_unique_numbers(element):
    unique = []
    for element in string:
        if elemtnt in unique:
            continue
        else:
            unique.append(element)
    return unique


print(get_unique_numbers(unique))



# 9 
def square(number):
    return number**2

numbers = [1, 2, 3, 4, 5, 6]

squared = map(square, numbers)

print(list(squared))



# 10 


coords = [(2, 8), (2, 3), (5, 3)]
result_square_distance = {point: (point[0] ** 2 + point[1] ** 2)**(0.5) for point in coords if point[1] == point[0] * 5 - 2}
print(result_square_distance)




# 11 
results = []
for i in range(2, 28):
    if i % 2 == 0:
        results.append(i**2)

print(results)



# 12 
coords = [(2, 8), (2, 3), (5, 3)]
result_square_distance = {point: (point[0] ** 2 + point[1] ** 2)**(0.5) for point in coords if point[1] > 0 and point[0] > 0}
print(max(result_square_distance, key =result_square_distance.get))
print(result_square_distance)



# 13 
nums_first = [1, 2, 3, 5, 8] 
nums_second = [2, 4, 8, 16, 32]


def f_13(a, b):
    sum_list = list(map(lambda x, y: x + y, nums_first , nums_second))
    minus_list = list(map(lambda x, y: x - y, nums_first , nums_second))  
    return [tuple([sum_list[i], minus_list[i]]) for i in range(len(sum_list))]
#list(map(..., nums_first, nums_second))

print( f_13(nums_first, nums_second))

