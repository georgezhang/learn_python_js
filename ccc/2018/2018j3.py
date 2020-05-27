line = input()
x = line.split(' ')

ab = int(x[0])
bc = int(x[1])
cd = int(x[2])
de = int(x[3])

aa = bb = cc = dd = ee = 0

print('%d %d %d %d %d' % (aa, ab, ab + bc, ab + bc + cd, ab + bc + cd + de))
print('%d %d %d %d %d' % (ab, bb, bc, bc + cd, bc + cd + de))
print('%d %d %d %d %d' % (ab + bc, bc, cc, cd, cd + de))
print('%d %d %d %d %d' % (ab + bc + cd, bc + cd, cd, dd, de))
print('%d %d %d %d %d' % (ab + bc + cd + de, bc + cd + de, cd + de, de, ee))