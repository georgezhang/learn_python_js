rules = []

for i in range(3):
    line = input()
    x = line.split()
    rules.append((x[0], x[1]))

line = input()
x = line.split()
S = int(x[0])
I = x[1]
F = x[2]

'''
print(rules)
print(S)
print(I)
print(F)
'''

# Look up for all possible rules
# convert recursive to bottom-up
output = []
def replace(str0, old, new, ind):
    return str0[:ind] + new + str0[ind + len(old):]

def findall(p, s):
    '''Yields all the positions of
    the pattern p in the str0ing s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

def applyRlue(str0, step):
    # over max steps
    if step > S:
        return False

    # find the rules
    j = 0   # index of the rules
    for r in rules:
        # find all matches?
        for ind in findall(r[0], str0):
            # apply rule and keep doing next level
            new_str0 = replace(str0, r[0], r[1], ind)

            # if match, found it
            if new_str0 == F:
                output.append([j+1, ind + 1, new_str0])
                return True
            else:
                new_step = step + 1
                result = applyRlue(new_str0, new_step)
                if result:
                    output.append([j+1, ind + 1, new_str0])
                    return True
        j = j + 1

    return False


applyRlue(I, 0)

# print(output)
for o in reversed(output):
    print(str(o[0]) + ' ' + str(o[1]) + ' ' + o[2])