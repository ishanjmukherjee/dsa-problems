# My solution
# Approach: Binary search up to the number itself, looking for n such that n^2 <= x but
#           (n + 1)^2 > x 

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
