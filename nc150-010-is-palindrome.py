# My solution using forward and backward pointers
# O(n) time complexity, where
# n : length of string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non-alphanumeric chars from the string
        s = "".join(c for c in s if c.isalnum()).lower()
        
        # initialize forward and backward pointers
        p1 = 0
        p2 = len(s) - 1

        # iterate until the pointers meet
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        
        return True

# The stupid simple, "cheating" solution using slicing
# O(n) time complexity, where
# n : length of string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()
        return s == s[::-1]

# Reimplementing official solution
# This uses constant memory (s[::-1] creates a new string)
# O(n) time complexity, where
# n : length of string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Custom helper function to determine if char is alphanumeric
        def isAlNum(c: chr) -> bool:
            return (ord('a') <= ord(c) <= ord('z') or
                    ord('A') <= ord(c) <= ord('Z') or
                    ord('0') <= ord(c) <= ord('9'))
        
        # Custom helper function to lowercase an uppercase char, else return 
        # the char itself
        def lower(c: chr) -> chr:
            if (ord('A') <= ord(c) <= ord('Z')):
                return chr(ord(c) - ord('A') + ord('a'))
            return c
        
        # Initializing pointers
        l = 0
        r = len(s) - 1

        # Iterating till pointers meet
        while l < r:
            # Finding next alphanumeric chars
            while l < r and not isAlNum(s[l]):
                l += 1
            while r > l and not isAlNum(s[r]):
                r -= 1
            
            if lower(s[l]) != lower(s[r]):
                return False
            l += 1
            r -= 1
        
        return True  

# New attempt: revisiting problem

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split()).lower()
        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
