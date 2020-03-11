numbers = [1, 2]
STEPS = 2

'''
[ 
    [1],
    [2]
]
'''
number_len = len(numbers)
out_list = []
for i in range(number_len):
    out_list.append([numbers[i]])
print('step 1:')
print(out_list)

'''
[
    [1, 1]
    [1, 2]
    [2, 1]
    [2, 2]
]
'''
out_list1 = []
for i in range(number_len):
    for j in range(len(out_list)):
        out_list1.append([numbers[i]] + out_list[j])
print('step 2:')
print(out_list1)

