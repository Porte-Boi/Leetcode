#include <bits/stdc++.h>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0, r = nums.size() - 1;
        int minNum = nums[0];

        while (l <= r){
            if (nums[l] < nums[r]){
                minNum = min(minNum, nums[l]);
                break;
            }

            int mid = l + (r - l) / 2;
            minNum = min(minNum, nums[mid]);

            if (nums[mid] >= nums[l]){
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return minNum;
    }
};
