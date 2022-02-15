from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        current_index = 0

        # using cyclic sort
        while current_index < len(nums):
            # correct index for current value
            correct_index = nums[current_index] - 1
            # if current value not at correct index,swap values
            if nums[current_index] != nums[correct_index]:
                nums[current_index], nums[correct_index] = nums[correct_index], nums[current_index]

                # if current value at correct position,move to next value and try to fix it
            else:
                current_index += 1

            # after placed all numbers at correct index
            # iterate over sorted array and find the mismatched positions
        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)
        return result
