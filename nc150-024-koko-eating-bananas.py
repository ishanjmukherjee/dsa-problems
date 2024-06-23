# My solution
# Approach: 
# Theoretical minimum speed: ceil(sum of all nums / h)
# Theoretical maximum speed: largest num in piles
# Binary search between the two extremes, checking if satisfied
# O(log n) time complexity, where
# n : largest number in piles

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # interesting note: a custom ceil() places the solution in the bottom ~5%
        # by runtime on Leetcode, while the ceil function from the math library
        # places the solution in the top ~10%. the custom ceil() *quadruples* the
        # runtime consistently.
        def ceil(x) -> int:
            # integer division rounds down
            # but, if the divisor is floating-point, integer dividing it yields a 
            # float; so, casting to int is necessary
            return int(x) if x % 1 == 0 else int(x // 1) + 1
        
        theoreticalMin = ceil(sum(piles) / h)
        theoreticalMax = max(piles)

        # binary search between the theoretical extrema
        l, r = theoreticalMin, theoreticalMax + 1
        ans = theoreticalMax # most pessimistic estimate for now
        while l < r:
            midVal = l + (r - l) // 2
            
            # compute hours taken at current speed being considered (midVal)
            hCurr = 0
            for pile in piles:
                # if pile finishes before the hour, the hour is still consumed
                # so, we ceil() the division
                hCurr += ceil(pile / midVal)
            if hCurr <= h: # valid speed is found
                ans = midVal # no need to set to min(ans, midVal) since we're 
                             # repeatedly decreasing speed anyway
                r = midVal
            else: # hCurr > h
                l = midVal + 1
        return ans
            
