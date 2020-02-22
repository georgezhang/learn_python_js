# first line
L = int(input())

# 9 +

# list
list = []

# input
for i in range(L):
    line = input()
    x = line.split()
    N = int(x[0])
    symbol = x[1]
    list.append((N, symbol))

# output
# print(list)
for line in list:
    print(line[1] * line[0])