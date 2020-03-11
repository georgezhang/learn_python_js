astr = 'lk;j;lk fieijlathe lkkthes'
substr = 'the'
alist = []

def getAllSubString(start):
    result = astr.find(substr, start)
    if result == -1:
        return False

    # print(result)
    alist.append(result)
    return getAllSubString(result + 1)

getAllSubString(0)
print(alist) # [0, 15, 51, 63, 83]