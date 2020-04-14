l1 = int(input())
l2 = int(input())
l3 = int(input())
l4 = int(input())

flag1 = False
flag2 = False
flag3 = False

if l1 == 8 or l1 == 9:
    flag1 = True

if l4 == 8 or l4 == 9:
    flag2 = True

if l2 == l3:
    flag3 = True

if flag1 and flag2 and flag3 :
    print('ignore')
else:
    print('answer')
