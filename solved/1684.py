from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0
        allowed_set = set(allowed)

        for word in words:
            if all(char in allowed_set for char in word):
                consistent += 1
            
        return consistent
