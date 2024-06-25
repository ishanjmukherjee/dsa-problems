# Reimplementing solution in video
# https://www.youtube.com/watch?v=1pkOgXD63yU
# O(n) time complexity, where
# n : length of prices

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            maxP = max(maxP, prices[r] - prices[l])
            if prices[r] <= prices[l]:
                l = r
            r += 1
        return maxP

# Reimplementing official (text) solution
# O(n) time complexity, where
# n : length of prices

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            maxP = max(maxP, price - lowest)
        return maxP
