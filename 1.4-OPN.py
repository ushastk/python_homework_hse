import math
s = input().split()
i = 0
while len(s) != 1:
    if s[i] == "*":
        elem = int(s[i-2]) * int(s[i - 1])
        s = s[:i-2] + [str(elem)] + s[i+1:]
        i -= 1

    elif s[i] == "+":
        elem = int(s[i-2]) + int(s[i - 1])
        s = s[:i-2] + [str(elem)] + s[i+1:]
        i -= 1


    elif s[i] == "-":
        elem = int(s[i-2]) - int(s[i - 1])
        s = s[:i-2] + [str(elem)] + s[i+1:]
        i -= 1

    elif s[i] == "/":
        elem = int(s[i-2]) // int(s[i - 1])
        s = s[:i-2] + [str(elem)] + s[i+1:]
        i -= 1


    elif s[i] == "~":
        elem = -int(s[i-1])
        s = s[:i-1] + [str(elem)] + s[i+1:]

    elif s[i] == "!":
        elem = math.factorial(int(s[i-1]))
        s = s[:i-1] + [str(elem)] + s[i+1:]

    elif s[i] == "#":
        elem = int(s[i-1])
        s = s[:i-1] + [str(elem)] + [str(elem)]+ s[i+1:]

    elif s[i] == '@':
        s  = s[:i - 3] + s[i - 2:i] + [s[i - 3]] + s[i + 1:]
        i -= 2

    else:
        i += 1

print(*s)