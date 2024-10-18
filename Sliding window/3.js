class Solution {
    lengthOfLongestSubstring(s) {
        const charSet = new Set();
        let l = 0;
        let maxLength = 0;

        for (let r = 0; r < s.length; r++) {
           
            while (charSet.has(s[r])) {
                charSet.delete(s[l]);
                l++;
            }

            charSet.add(s[r]);

            maxLength = Math.max(maxLength, r - l + 1);
        }

        return maxLength;
    }
}