class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int maxP = 0;

        while(right<prices.length){ // until we touch the bound
            if(prices[left]<prices[right]){ //if the buy price is smaller than the selling price
                int profit = prices[right] - prices[left];  // we calculate the profit
                maxP = Math.max(maxP,profit);   // check if the current profit is max or not
            }
            else{   // if the buy price is greater than the selling price, we change the left to right
                left = right;
            }
            right+=1;   // also we increment right anyway until we reach the bound
        }
        return maxP;    // returning the maximum profit
    }
}