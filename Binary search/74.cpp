#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;

        int rows = matrix.size();
        int columns = matrix[0].size();

        int l = 0;
        int r = rows * columns - 1;

        while (l <= r){
            int mid = l + (r - l) / 2;
            int mid_value = matrix[mid / columns][mid % columns];

            if (mid_value == target){
                return true;
            } else if (mid_value < target){
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return false;
    }
};