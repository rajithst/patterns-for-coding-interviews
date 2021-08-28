from typing import List

arr = [2, 3, 4, 1, 5]
sub_array_size = 2

max_sum = 0
window_start = 0
window_sum = 0.0
for window_end in range(len(arr)):
    window_sum += arr[window_end]

    if window_end >= sub_array_size - 1:
        max_sum = max(window_sum, max_sum)
        window_sum -= arr[window_start]
        window_start += 1
print(max_sum)
