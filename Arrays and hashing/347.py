from collections import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        occurence = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            occurence[c].append(n)
        
        res = []

        for i in range(len(occurence) - 1, 0, -1):
            for n in occurence[i]:
                res.append(n)
                if len(res) == k:
                    return res

        