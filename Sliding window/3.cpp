#include <bits/stdc++.h>
#include <unordered_set>
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> uniqe;
        int l = 0;
        int sub_str_length = 0;
        for (int r = 0; r < s.size(); r++){
            while (uniqe.find(s[r]) != uniqe.end()){
                uniqe.erase(s[l]);
                l++;
            }
            uniqe.insert(s[r]);
            sub_str_length = max(sub_str_length, r - l + 1);
        }
        return sub_str_length;
    }
};