g = [1, 2, 3, 4]

def flip(g, input):
    if input == 'H':
        # horizontal
        g = [g[2],g[3],g[0],g[1]]
    elif input == 'V':
        # vertical
        g = [g[1],g[0],g[3],g[2]]
    else:
        pass
    return g

# get inputs from file
inputs = input()

# process
for input in inputs:
    g = flip(g, input)

# output
print("%d %d\n%d %d" % (g[0], g[1], g[2], g[3]))