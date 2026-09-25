class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell = 1
        maxProfit = 0
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell = buy+1
            else:
                maxProfit = max(maxProfit,prices[sell] - prices[buy])
                sell+=1        

        return maxProfit