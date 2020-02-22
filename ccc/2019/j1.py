scores = []

for i in range(6):
    inp = int(input())
    scores.append(inp)

a = scores[0] * 3 + scores[1] * 2 + scores[2] * 1
b = scores[3] * 3 + scores[4] * 2 + scores[5] * 1

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('T')