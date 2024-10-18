class Solution:
    # The list int method declaring the variable and return val in list
    def two_sum(self, nums: list[int], target: int) -> list[int]:

        # This dictionary is for store data
        seen = {}

        for i, val in enumerate(nums):
            remains = target - val

            if remains in seen:
                return [seen[remains], i]
            
            seen[val] = i
print(Solution().two_sum([2,7,11,15], 9))