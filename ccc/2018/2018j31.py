x = [3, 10, 12, 5]

# index 0 to 3
# 2 numbers call a function, this function
# will return the distance of those two cities
def getDistance(start, end):
    # I got answer, I will just return it. Dynamic Programming
    if start == end:
        return 0

    distance = 0
    index = start
    while index < end:
        distance = distance + x[index]
        index = index + 1
    return distance

print(getDistance(0, 1))

