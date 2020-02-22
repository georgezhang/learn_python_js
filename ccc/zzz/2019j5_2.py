olds = []
news = []

for i in range(3):
    line = input()
    x = line.split()
    olds.append((x[0], len(x[0])))
    news.append((x[1], len(x[1])))

# print(olds)
# print(news)

line = input()
x = line.split()
S = int(x[0])
I = x[1]
F = x[2]

# Look up for all possible rules
# convert recursive to bottom-up
output = []
def replace(str0, old, new, ind):
    return str0[:ind] + new + str0[ind + len(old):]

def find_all(str0):
    i = 0
    pos = [] # (Pi, Ri)
    while i < len(str0):
        if str0[i: i + olds[0][1]] == olds[0][0]:
           pos.append((i, 0))
        if str0[i: i + olds[1][1]] == olds[1][0]:
           pos.append((i, 1))
        if str0[i: i + olds[2][1]] == olds[2][0]:
           pos.append((i, 2))
        i = i + 1
    return pos

def applyRlue(str0, step):
    # over max steps
    if step > S - 1:
        return False

    # find all matches?
    matches = find_all(str0)
    for (p, r) in matches:
        # apply rule and keep doing next level
        new_str0 = replace(str0, olds[r][0], news[r][0], p)

        # if match, found it in exact steps
        if new_str0 == F and step == S - 1:
            output.append([r+1, p + 1, new_str0])
            return True
        else:
            new_step = step + 1
            result = applyRlue(new_str0, new_step)
            if result:
                output.append([r+1, p + 1, new_str0])
                return True

    return False


applyRlue(I, 0)

# print(output)
for o in reversed(output):
    print(str(o[0]) + ' ' + str(o[1]) + ' ' + o[2])