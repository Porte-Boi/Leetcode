class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub_str_lenght = 0
        uniqe = set()
        
        for r in range(len(s)):
            while s[r] in uniqe:
                uniqe.remove(s[l])
                l += 1
            
            uniqe.add(s[r])
            sub_str_lenght = max(sub_str_lenght, r - l + 1)
                
        return sub_str_lenght


