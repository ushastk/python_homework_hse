import csv
with open('2.6-alpha_oriona.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    data = []
    for elem in reader:
        data.append(elem)

length = 1
max_length = 1
line = 0
max_line = 0
for i in range(1, len(data)):
    if int(data[i]['luminosity']) <= int(data[i-1]["luminosity"]):
        length += 1

    else:
        if max_length < length:
            max_length = length
            max_line = line
        length = 1
        line = i

with open("result.txt", "w", encoding="UTF-8") as f:
    f.write(str(max_length) + '\n' + data[max_line]["date"] + " " + data[max_line]['time'])
#print(max_length, data[max_line]['date'], data[max_line]["time"])