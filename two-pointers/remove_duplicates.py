arr = [2, 3, 3, 3, 6, 9, 9]
p1 = 0
p2 = 1

for i in range(1, len(arr)):
    if arr[p1] != arr[p2]:
        arr[p1 + 1] = arr[p2]
        p1 += 1
    p2 += 1
print(arr[:p1+1])