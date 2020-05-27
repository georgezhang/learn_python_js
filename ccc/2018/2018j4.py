N = int(input())
table2d = []
def conv(strl):
    result = []
    for s in strl:
        result.append(int(s))
    return result

for i in range(N):
    line = input()
    row = conv(line.split(' '))
    table2d.append(row)

# print(table2d)
#left top
lt = table2d[0][0]
# right top
rt = table2d[0][N - 1]
# left bottom
lb = table2d[N - 1][0]
# right bottom
rb = table2d[N - 1][N - 1]

output = []

if lt < rt and lt < lb and lt < rb:
    # print('left top')
    output = table2d
elif rt < lt and rt < lb and rt < rb:
    # print('right top')
    for r in range(N):
        rowout = []
        for p in range(N):
            rowout.append(table2d[p][N - r - 1])
        output.append(rowout)
elif lb < lt and lb < rt and lb < rb:
    # print('left bottom')
    for r in range(N):
        rowout = []
        for p in range(N):
            rowout.append(table2d[N - p - 1][r])
        output.append(rowout)
elif rb < lt and rb < rt and rb < lb:
    # print('right bottom')
    for r in range(N):
        rowout = []
        for p in range(N):
            rowout.append(table2d[N - r - 1][N - p - 1])
        output.append(rowout)
else:
    print('something wrong')

# print(output)

# output
for r in output:
    print(' '.join(map(str, r)))
