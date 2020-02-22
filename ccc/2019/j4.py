a = 1
b = 2
c = 3
d = 4

def h_flip():
    t = 0
    t = a
    a = c
    c = t

    t = b
    b = d
    d = t

def v_flip():
    pass

print("%d %d" % (a, b))
print("%d %d" % (c, d))