'''
if the next charactor is the same, then count 1 more
if the next charactor is not the same, then output, and reset count = 1
if the next charactor is the end, then output and reset count
'''

def zip(line):
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
        elif line[i] == line[i + 1]:
            count = count + 1
        i = i + 1
    return result

N = int(input()) # first line
output = [] # all output from zip
for j in range(N):
    l = input()
    output.append(zip(l))

# output
for o in output:
    print(o)
