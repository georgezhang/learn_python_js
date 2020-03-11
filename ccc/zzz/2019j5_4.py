def getRules():
    line = input()
    x = line.split()
    return x[0], x[1]


RULE = []
RULE[0] = getRules()
RULE[1] = getRules()
RULE[2] = getRules()

line4 = (input()).split()
STEPS = int(line4[0])
INPUT = line4[1]
OUTPUT = line4[2]

# find all possibilities
allPoss = []

def addOneMoreStep(poss, step):
    if step > STEPS:
        return poss

    newPoss = []
    for i in range(3):
        subPoss = []
        for j in range(len(poss)):
            subPoss.append([RULE[i]] + poss[j])
        newPoss.append(subPoss)
    addOneMoreStep(newPoss, step + 1)

for p in addOneMoreStep([], 0):
    print(p)