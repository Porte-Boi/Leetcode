from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = [(carPos, sph) for carPos, sph in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []

        for carpos, sph in pairs:
            stack.append((target - carpos) / sph)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
        

        
