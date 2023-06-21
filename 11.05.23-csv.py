def my_sort_data(path_to_data):

  import csv

  with open(path_to_data, 'r') as f:
      lines = [line.strip() for line in f.readlines()]

  data = [(line.split(': ')[0], line.split(': ')[1]) for line in lines]

  sorted_data = sorted(data, key=lambda x: x[0])

  with open('output.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['name', 'grade'])
    for row in sorted_data:
        writer.writerow(row)

path_to_data = "/content/data.txt"
result = my_sort_data(path_to_data)

import unittest

def test_sort_data(self):

  path_to_data = "/content/data.txt"
  result = my_sort_data(path_to_data)

  first = """name,grade
Белова Юлия,3
Белогур Алексей,3
Даниил Бакушкин,3
Зисман Илья,3
Зосимов Кирилл,3
Кабардиева Камилла,3
Кленков Андрей,4
Кольтюгин Максим,3
Котов Алексей,3"""