from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))
    print(s.containsDuplicate([1, 2, 3, 4]))
        