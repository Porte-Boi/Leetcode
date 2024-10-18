from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        l_s = 0

        for n in nums:
            if n-1 not in numset:
                length = 0
                while (n+length) in numset:
                    length += 1
                l_s = max(length, l_s)

        return l_s