from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
