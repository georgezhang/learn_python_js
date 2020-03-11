members = [1, 2, 3]
STEPS = 2

'''
[
    [1, 1, 1],
    [1, 1, 2],
    [1, 1, 3],
    ....
]    

1. [[1], [2], [3]], loop all members to create the list
2. [
     [1, 1], [1, 2], [1, 3],
     [2, 1], [2, 2], [2, 3],
    ]
from step 1, we loop all members, prepend the to them each time
3. simplify the process
4. find out the way to do all 3 steps
'''
out_list = []
m_len = len(members)

for i in range(m_len):
    out_list.append([members[i]])
print('out_list')
print(out_list)

out_list1 = []
for i in range(m_len):
    for j in range(len(out_list)):
        out_list1.append([members[i]] + out_list[j])

print('out_list1')
print(out_list1)

out_list2 = []
for i in range(m_len):
    for j in range(len(out_list1)):
        out_list2.append([members[i]] + out_list1[j])

print('out_list2')
print(out_list2)

'''
output as the next level's output
'''

def bunce(out_list_n, step):
    if (step > STEPS):
        return out_list_n

    out_list_n_1 = []
    if len(out_list_n) == 0:
        for i in range(m_len):
            out_list_n_1.append([members[i]])
    else:
        for i in range(m_len):
            for j in range(len(out_list_n)):
                out_list_n_1.append([members[i]] + out_list_n[j])
    print('step:' + str(step))
    print(out_list_n_1)
    return bunce(out_list_n_1, step + 1)

print(bunce([], 1))