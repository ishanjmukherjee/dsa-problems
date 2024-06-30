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

# New attempt 1: revisiting
# Reimplementing official solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            maxProfit = max(maxProfit, price - lowest)
        return maxProfit

# New attempt 1: revisiting
# Coding up the more explicit sliding window solution after looking at
# the pithy official text solution and reimplementing it (above)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxProfit = 0
        while r < len(prices):
            while prices[l] > prices[r]:
                l += 1
            maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        return maxProfit

# New attempt 1: revisiting
# Optimizing the explicit sliding window solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        maxProfit = 0
        while r < len(prices):
            # no need to step l to r; just set l = r
            if prices[l] > prices[r]:
                l = r
            maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        return maxProfit
