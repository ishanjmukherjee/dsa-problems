# Reimplementing a solution
# https://leetcode.com/problems/longest-harmonious-subsequence/solutions/103534/python-straightforward-with-explanation

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        countNums = {}
        ans = 0
        for num in nums:
            countNums[num] = countNums.get(num, 0) + 1
        for num in nums:
            if num + 1 in countNums:
                ans = max(ans, countNums[num] + countNums[num + 1])
        return ans
