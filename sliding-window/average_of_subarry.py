from typing import List

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
sub_array_size = 5

results: List[float] = []
window_start = 0
window_sum = 0.0
for window_end in range(len(arr)):
    window_sum += arr[window_end]

    if window_end >= sub_array_size - 1:
        results.append(window_sum)
        window_sum -= arr[window_start]
        window_start += 1
print(results)