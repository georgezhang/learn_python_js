astr = 'AAABBBCCCXYZBBB123BBBLJIJIJI'
substr = 'BBB'
sub2 = 'XXXX'
alist = []

def getAllSubString(start):
    result = astr.find(substr, start)
    if result == -1:
        return False

    # print(result)
    alist.append(result)
    return getAllSubString(result + 1)

getAllSubString(0)
print(alist) # [3, 12, 18]

# print(input1[0:position0] + sub2 + input1[position0 + l1:pos2] + sub2 + input1[pos2 + 3:])
def replaceStr(start, pos):
    return astr[start : pos]

'''
x = replaceStr(0, 3)
print(x)
y = replaceStr(3 + len(substr), 12)
print(y)
z = replaceStr(12 + len(substr), 18)
print(z)
'''
list1 = []
start = 0
for i in alist:
    list1.append(replaceStr(start, i))
    print(replaceStr(start, i))
    start = i + len(substr)
list1.append(astr[start :])
print(list1)
output = ''
count = 0
for j in list1:
    count = count + 1
    output = output + j
    if count < len(list1):
        output = output + sub2
print(output)