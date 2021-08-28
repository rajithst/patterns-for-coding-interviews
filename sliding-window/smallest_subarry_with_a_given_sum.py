"""
Given an array of positive numbers and a positive number ‘S,’
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
"""
import math

arr = [3, 4, 1, 1, 6]
given_sum = 8
window_start = 0
window_sum = 0.0
min_length = math.inf

#iterate through array
for window_end in range(len(arr)):
    #keep collecting sum of running window
    window_sum += arr[window_end]
    #while window sum is greater than given sum,shrinking the window
    while window_sum >= given_sum:
        #update the min length of the window
        min_length = min(min_length, window_end - window_start + 1)
        #remove start window value from window sum
        window_sum -= arr[window_start]
        #move start window to forward
        window_start += 1
if min_length == math.inf:
    min_length = 0

print(min_length)
