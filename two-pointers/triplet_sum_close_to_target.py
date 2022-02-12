from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # sort array first to apply two sum technique
        nums_sorted = sorted(nums)
        minimum_diff = float("inf")
        for i in range(len(nums) - 2):

            # define left pointer as next to current value and right pointer for end of the list
            left_pointer = i + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                # compute the difference
                diff = target - (nums_sorted[i] + nums_sorted[left_pointer] + nums_sorted[right_pointer])
                # if difference is 0,it's the best value can get
                if diff == 0:
                    return target
                # if current difference is lower than sofar,update minimum difference
                if abs(diff) < abs(minimum_diff):
                    minimum_diff = diff
                # if difference is greater than 0,we need a bigger triplet sum to minimize the difference
                # since array is sorted,we can move left pointer forward to find a bigger triplet
                if diff > 0:
                    left_pointer += 1
                # else we need a smaller sum
                else:
                    right_pointer -= 1

        return target - minimum_diff
