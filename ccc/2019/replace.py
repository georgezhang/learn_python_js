'''
INPUT:
AAA BBB CCC
BBB
XXXX
AAA + XXXX + CCC

OUTPUT:
AAAXXXXCCC
'''

input1 = 'AAABBBCCCXYZBBB123BBBLJIJIJI'
sub1 = 'BBB'
sub2 = 'XXXX'
position0 = input1.find('BBB')
print(position0)
l1 = len(sub1)
print(position0 + l1)
print(input1[0:position0])
print(input1[position0 + l1:])
print(input1[0:position0] + sub2 + input1[position0 + l1:])
pos2 = input1.find('BBB', position0 + 1)
print(pos2)
print(input1[0:position0] + sub2 + input1[position0 + l1:pos2] + sub2 + input1[pos2 + 3:])