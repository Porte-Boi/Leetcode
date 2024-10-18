from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        n = len(arr)
        prefix_xor = [0] * (n + 1)

        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        res = []

        for l, r in queries:
            res.append(prefix_xor[r+1] ^ prefix_xor[l])

        return res
