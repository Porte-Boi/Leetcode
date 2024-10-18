#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>& A = nums1;
        vector<int>& B = nums2;
        int m = A.size();
        int n = B.size();
        
        // Ensure A is the smaller array
        if (m > n) {
            return findMedianSortedArrays(B, A);
        }
        
        int total = m + n;
        int half = (total + 1) / 2;
        
        int l = 0, r = m;
        double result = 0.0;

        while (l <= r) {
            int i = l + (r - l) / 2;  // Partition point for A
            int j = half - i;         // Partition point for B

            // Handle boundary conditions for A
            int Aleft = (i > 0) ? A[i - 1] : INT_MIN;
            int Aright = (i < m) ? A[i] : INT_MAX;
            
            // Handle boundary conditions for B
            int Bleft = (j > 0) ? B[j - 1] : INT_MIN;
            int Bright = (j < n) ? B[j] : INT_MAX;
            
            // Check if the partition is valid
            if (Aleft <= Bright && Bleft <= Aright) {
                // If total number of elements is odd
                if (total % 2 == 1) {
                    result = max(Aleft, Bleft);
                } 
                // If total number of elements is even
                else {
                    result = (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0;
                }
                break;
            } 
            // Adjust binary search based on invalid partition
            else if (Aleft > Bright) {
                r = i - 1; // Move the partition to the left
            } else {
                l = i + 1; // Move the partition to the right
            }
        }
        
        return result;
    }
};
