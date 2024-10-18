from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        minNum = float('inf')

        while l <= r:

            if nums[r] >= nums[l]:
                minNum = min(minNum, nums[l])
                break

            mid = l + (r - l) // 2

            minNum = min(minNum, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            
        return minNum

