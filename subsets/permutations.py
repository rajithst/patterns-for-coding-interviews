from collections import deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        permutations = deque()
        permutations.append([])
        # iterate over numbers and add this number to every position of each permutation
        for num in nums:

            times = len(permutations)
            for _ in range(times):

                # get current permutation
                current = permutations.popleft()

                # add number to each position of the permutation
                for i in range(len(current) + 1):
                    current_copy = current.copy()
                    current_copy.insert(i, num)
                    if len(current_copy) == len(nums):
                        result.append(current_copy)
                    else:
                        permutations.append(current_copy)
        return result
