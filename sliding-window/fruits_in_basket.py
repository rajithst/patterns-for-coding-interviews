# https://leetcode.com/problems/fruit-into-baskets/

fruits = ['A', 'B', "A", "B", 'C', 'A', 'C', "C", "A"]
window_start = 0
fruits_count = {}
baskets = 2
max_len = 0
for window_end in range(len(fruits)):
    fruit = fruits[window_end]

    if fruit not in fruits_count:
        fruits_count[fruit] = 0
    fruits_count[fruit] += 1

    while len(fruits_count) > baskets:
        remove = fruits[window_start]
        fruits_count[remove] -= 1
        if fruits_count[remove] == 0:
            del fruits_count[remove]
        window_start += 1

    max_len = max(max_len, window_end - window_start + 1)

print(max_len)
