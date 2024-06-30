# My solution after watching verbal explanation in solution video
# (up to 3:26)
# https://www.youtube.com/watch?v=UbyhOgBN834
# O(26 * n) = O(n) time complexity, where
# n : length of s1

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # dictionarize s1
        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        
        # dictionarize s1-length substrings of s2; if the dictionaries 
        # representing s1 and the substring equal, permutation found
        count2 = {}
        l = 0
        for r in range(len(s2)): 
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            # advance l only if substring reach len(s1)
            if r - l + 1 > len(s1):
                count2[s2[l]] -= 1
                # need to pop otherwise 0 values remain and dictionary
                # equality in count1 == count2 fails
                if count2[s2[l]] == 0:
                    count2.pop(s2[l])
                l += 1
            if count1 == count2:
                return True
        return False

# My solution with pithier assignment of l

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = count1.get(c, 0) + 1
        
        count2 = {}
        for r in range(len(s2)): 
            l = max(r - len(s1), 0) # pithier assignment of l
            count2[s2[r]] = count2.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    count2.pop(s2[l])
            if count1 == count2:
                return True
        return False

# Reimplementing official solution
# "True" sliding window, maintains matches and doesn't compare entire
# substring with s1 each time the window shifts
# So, it's more efficient than the O(26 * n) solution
# O(n) time complexity, where
# n : length of s2 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        # if s2 is longer, it cannot possibly contain a permutation of s1
        if len(s2) < len(s1):
            return False
        
        count1, count2 = {}, {}
        for i in range(len(s1)):
            count1[s1[i]] = count1.get(s1[i], 0) + 1
            count2[s2[i]] = count2.get(s2[i], 0) + 1
        matches = 0
        for i in range(26):
            c = chr(i + ord('a'))
            count1[c] = count1.get(c, 0)
            count2[c] = count2.get(c, 0)
            matches += 1 if count1[c] == count2[c] else 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            count2[s2[r]] += 1
            if count2[s2[r]] == count1[s2[r]]:
                matches += 1
            elif count2[s2[r]] - 1 == count1[s2[r]]:
                matches -= 1
            
            # pithy assignment of l; differs from official solution
            l = r - len(s1) 
            count2[s2[l]] -= 1
            if count2[s2[l]] == count1[s2[l]]:
                matches += 1
            elif count2[s2[l]] + 1 == count1[s2[l]]:
                matches -= 1
        return matches == 26
