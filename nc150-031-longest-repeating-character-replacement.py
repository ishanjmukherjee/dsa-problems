# Reimplementing a solution
# https://leetcode.com/problems/longest-repeating-character-replacement/solutions/765776/python-two-pointers-process-for-coding-interviews
# O(n) time complexity, where
# n : length of s

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestLen = 0
        l = 0
        cFreq = {}
        for r in range(len(s)):
            cFreq[s[r]] = cFreq.get(s[r], 0) + 1
            cellsCount = r - l + 1
            # max(cFreq.values()) is O(1) time since cFreq has only 26
            # (not O(n)) keys
            if cellsCount - max(cFreq.values()) <= k:
                longestLen = max(longestLen, cellsCount)
            else:
                cFreq[s[l]] -= 1
                l += 1
        return longestLen

# Reimplementing official solution
# O(n) time complexity, where 
# n : length of s

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]]) 

            if r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
        return r - l + 1 # don't need to track maxLen because l is 
                         # incremented on every loop iteration after
                         # maximum-length substring is found

# New attempt 1: revisiting
# Reimplementing official solution

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cFreqs = {}
        maxf = 0
        l = 0
        for r in range(len(s)):
            cFreqs[s[r]] = cFreqs.get(s[r], 0) + 1
            maxf = max(maxf, cFreqs[s[r]])
            if r - l + 1 - maxf > k:
                cFreqs[s[l]] -= 1
                l += 1
        return r - l + 1
