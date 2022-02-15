from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        current_index = 0
        # use cyclic sort to place values in correct order
        while current_index < len(nums):
            # get index for current index
            correct_index = nums[current_index] - 1
            # if current value is not in correct index,swap values
            if nums[current_index] != nums[correct_index]:
                nums[current_index], nums[correct_index] = nums[correct_index], nums[current_index]
            # if current value is in correct position,move pointer to next value to fix
            else:
                current_index += 1
        # after all values placed in the correct indexes,duplicate values are mismatching indexes and values
        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
        return result
