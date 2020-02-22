X = "ABCBDAB"
Y = "BDCABA"
lookup = {}

def lcs(m, n):
    if m == 0 or n == 0:
        return 0

    key = str(m) + '|' + str(n)

    if key not in lookup:
        if X[m-1] == Y[n-1]:
            lookup[key] = lcs(m-1, n-1) + 1
        if X[m-1] != Y[n-1]:
            lookup[key] = max(lcs(m, n-1), lcs(m-1, n))

    return lookup[key]

print(lcs(len(X), len(Y)))