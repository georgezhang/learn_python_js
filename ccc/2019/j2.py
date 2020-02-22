print("+" * 9)

L = int(input())

list = []

#input
for i in range(L):
    line = input()
    x = line.split()
    N = int(x[0])
    symbol = x[1]
    list.append((N, symbol))

# output
for line in list:
    print(line[1] * line[0])