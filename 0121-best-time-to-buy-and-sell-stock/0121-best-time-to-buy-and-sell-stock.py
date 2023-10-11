class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float("inf")
        maxProfit=0
        for i in range(len(prices)):
            min_price=min(min_price, prices[i])
            maxProfit=max(maxProfit, prices[i]-min_price)
            
        return maxProfit