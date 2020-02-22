b = 'A cat is chasing a hat.'
b_len = len(b)

count = 0
j = 0
while j < b_len:
    i = b[j]
    if i == 'A' or i == 'a':
        count = count + 1
    j = j + 1

print(count)

