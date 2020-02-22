olds = [('AA', 2), ('AB', 2), ('B', 1)]
min_old = 1
visited = {}

def find_match(str1, i):
    if len(str1) < min_old:
        return []

    if str1 in visited:
        return [(i + v[0], v[1]) for v in visited[str1]]

    pos = []
    if str1[0: olds[0][1]] == olds[0][0]:
        pos.append((i, 0))
    if str1[0: olds[1][1]] == olds[1][0]:
        pos.append((i, 1))
    if str1[0: olds[2][1]] == olds[2][0]:
        pos.append((i,2))
    pos = pos + find_match(str1[1:], i + 1)

    visited[str1] = pos # store for subsequnce search
    return pos

print(find_match('AB', 0))