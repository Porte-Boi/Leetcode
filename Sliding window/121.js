/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let l = 0, r = 1;
    let max_profit = 0;

    while (r < prices.length){
        if (prices[l] < prices[r]){
            max_profit = Math.max(max_profit, prices[r] - prices[l]);
        } else {
            l = r;
        }
        r++;
    }
    return max_profit;
};