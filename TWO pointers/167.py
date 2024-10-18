from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            char_sum = numbers[l] + numbers[r]

            if char_sum < target:
                l += 1
            elif char_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]