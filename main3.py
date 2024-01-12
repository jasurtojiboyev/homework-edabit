list = [4, 3, 2, 5, 1, 6, 10, 9, 8, 7]

n = len(list)
for x in range(n):
    for y in range(0, n - x - 1):
        if list[y] > list[y + 1]:
            list[y], list[y + 1] = list[y + 1], list[y]
print(list)



a = max(list)