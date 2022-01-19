
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
window_start = 0
ones_count = 0
max_freq = 0
max_len = 0
for window_end in range(len(nums)):
    char = nums[window_end]
    if char == 1:
        ones_count += 1

    max_freq = max(max_freq, ones_count)
    while window_end - window_start + 1 - ones_count > k:
        rem = nums[window_start]
        if rem == 1:
            ones_count -= 1
        window_start += 1

    max_len = max(max_len, window_end - window_start + 1)
print(max_len)