# My solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Helper function to convert string to dict
        # Key is char in the string and value is number of occurrences  
        def toDict(st: str) -> dict:
            st_dict = {}
            for c in st:
                if c in st_dict:
                    st_dict[c] += 1
                else:
                    st_dict[c] = 1
            return st_dict
        
        sDict = toDict(s)
        tDict = toDict(t)
        return sDict == tDict

# Reimplementing official solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i], 0) + 1
            tDict[t[i]] = tDict.get(t[i], 0) + 1
        
        return sDict == tDict  
