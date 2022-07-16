class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left pointer buys, right pointer sells
        maxP = 0
        
        while r < len(prices):
            # determine profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
            
        return maxP