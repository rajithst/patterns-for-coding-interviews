arr = [-2, -1, 0, 2, 3]
p1 = 0
p2 = len(arr) - 1
result = [0] * len(arr)
count = len(arr) - 1
while p1 <= p2:
    if abs(arr[p1]) > abs(arr[p2]):
        result[count] = arr[p1] * arr[p1]
        p1 += 1
    else:
        result[count] = arr[p2] * arr[p2]
        p2 -= 1
    count -= 1
print(result)
