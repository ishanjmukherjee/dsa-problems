# Brute force
# Takes ~7x as long as the median Leetcode submission
# O(n^2) time complexity, where
# n : length of s

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        while l <= len(s) - 1:
            r = l + 1
            while r <= len(s) - 1 and s[r] not in s[l:r]:
                r += 1
            ans = max(ans, r-l)
            l += 1
        return ans

# Reimplementing official solution
# O(n) time complexity, where
# n : length of s 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            ans = max(ans, r - l + 1)
        return ans
