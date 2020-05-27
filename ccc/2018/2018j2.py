N = int(input())
y = input()
t = input()

count = 0

def spot(p, i):
    return p[i : i + 1] == 'C'

for i in range(N):
    if spot(y, i) and spot(t, i):
        count = count + 1

print(count)

