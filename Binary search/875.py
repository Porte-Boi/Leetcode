from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        min_h = r

        while l <= r:
            k = l + (r - l) // 2

            totalTime = 0

            for banana in piles:
                totalTime += math.ceil(float(banana) / k)
            
            if totalTime <= h:
                min_h = min(min_h, k)
                r = k - 1
            else:
                l = k + 1
        
        return min_h

