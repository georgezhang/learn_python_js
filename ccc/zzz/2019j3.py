def zip(line):
    first = line[0:1]
    for c in line:
        print(c)

def zip2(line):
    len_line = len(line)
    i = 0
    while i < len_line:
        print(line[i])
        i = i + 1

'''
if the next charactor is the same, then count 1 more
if the next charactor is not the same, then output to result, and reset it
if the next charactor is the end, then output to result, and reset it
'''
def zip3(line):
    len_line = len(line)
    i = 0
    count = 1
    while i < len_line:
        if i + 1 == len_line or line[i] != line[i + 1]:
            print(count)
            print(line[i])
            count = 1
        else:
            count = count + 1
        i = i + 1

# zip3('aaaabbcdd')

def zip4(line):
    len_line = len(line)
    result = ''
    i = 0
    count = 1
    while i < len_line:
        if i + 1 == len_line or line[i] != line[i + 1]:
            if len(result) != 0:
                result = result + ' '
            result = result + str(count) + ' ' + line[i]
            count = 1
        else:
            count = count + 1
        i = i + 1
    return result

# print(zip4('aaaabbcdd'))

N = int(input())
output = []
for j in range(N):
    l = input()
    output.append(zip4(l))

for o in output:
    print(o)