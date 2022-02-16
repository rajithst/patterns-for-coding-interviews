from typing import List

"""Once we are done with the cyclic sort, we will iterate through the array to find the number that is not at the 
correct index. Since only one number got corrupted, the number at the wrong index is the duplicated number and the 
index itself represents the missing number. """


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        current_index = 0
        while current_index < len(nums):
            correct_index = nums[current_index] - 1
            if nums[current_index] != nums[correct_index]:
                nums[current_index], nums[correct_index] = nums[correct_index], nums[current_index]
            else:
                current_index += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
        return [-1, -1]
