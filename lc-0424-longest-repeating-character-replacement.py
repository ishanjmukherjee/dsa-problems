# Reimplementing a solution
# https://leetcode.com/problems/longest-repeating-character-replacement/solutions/765776/python-two-pointers-process-for-coding-interviews
# Probably O(n^2) due to max(cFreq.values()), where
# n : length of s

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestLen = 0
        l = 0
        cFreq = {}
        for r in range(len(s)):
            cFreq[s[r]] = cFreq.get(s[r], 0) + 1
            cellsCount = r - l + 1
            if cellsCount - max(cFreq.values()) <= k:
                longestLen = max(longestLen, cellsCount)
            else:
                cFreq[s[l]] -= 1
                l += 1
        return longestLen

  # TODO: implement optimal solution

