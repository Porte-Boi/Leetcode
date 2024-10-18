#include <bits/stdc++.h>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(), piles.end());
        int min_h = r;

        while (l <= r){
            int k = l + (r - l) / 2;

            long int totalTime = 0;

            for (int banana : piles){
                totalTime += (banana + k - 1) / k;
            }

            if (totalTime <= h){
                min_h = min(min_h, k);
                r = k - 1;
            } else {
                l = k + 1;
            }
        }
        return min_h;
    }
};