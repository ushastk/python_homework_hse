from sys import stdin
print("Введите cntrl+D, чтобы закончить ввод.")
lines = []
for line in stdin:
    lines.append(line.rstrip("\n").lstrip())
#print(lines)

for i in range(1, len(lines)+1):
    if lines[i-1][0] == '#':
        print(f'Line {i}: {lines[i-1].lstrip("#").lstrip()}')