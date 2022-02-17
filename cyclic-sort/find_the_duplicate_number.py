from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        current_index = 0

        # cyclic sort to place values in correct position
        while current_index < len(nums):
            # correct index for current value
            correct_index = nums[current_index] - 1
            # if current value not in correct position,swap values
            if nums[current_index] != nums[correct_index]:
                nums[current_index], nums[correct_index] = nums[correct_index], nums[current_index]

            # if current value is at correct position,move to next position for fix
            else:
                current_index += 1

        # since array has only one duplicate value,iterate through sorted array  and return the first mismatching value
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]
