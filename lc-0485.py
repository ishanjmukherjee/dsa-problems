# My solution
# Approach: linear search for the longest 1-string
# O(n) time complexity, where
# n : length of nums 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        currCount = 0
        for num in nums:
            if num == 1:
                currCount += 1
            else: # num == 0
                ans = max(ans, currCount)
                currCount = 0
        ans = max(ans, currCount) # edge case where nums ends with longest 1-sequence
        return ans
