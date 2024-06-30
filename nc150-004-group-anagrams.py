# Brute force using isAnagram
# O(n^2 * k) time complexity, where
# n : number of elements in strs
# k : length of an element in strs

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Helper returns whether string arguments are anagrams 
        def isAnagram(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            sDict = {}
            tDict = {}

            for i in range(len(s)):
                sDict[s[i]] = sDict.get(s[i], 0) + 1
                tDict[t[i]] = tDict.get(t[i], 0) + 1

            return sDict == tDict
        
        anagramGroups = []
        for s in strs:
            # initialize flag
            isAnag = False
            # is is anagram, add to anagram group
            for i in range(len(anagramGroups)):
                if isAnagram(s, anagramGroups[i][0]):
                    isAnag = True
                    anagramGroups[i].append(s)
            
            # if isn't flag, create new anagram group
            if not isAnag:
                anagramGroups.append([s])
        return anagramGroups

# Reimplementing official solution
# O(n * k) time complexity, where
# n : number of elements in strs
# k : length of an element in strs

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagramGroups[tuple(count)].append(s)
        return anagramGroups.values()  

# New attempt: revisiting

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)
        for s in strs:
            sDict = [0] * 26
            for c in s:
                sDict[ord(c) - ord('a')] += 1
            # I forgot this trick to tuple() the list to make it immutable
            # and thus a valid key
            anagramDict[tuple(sDict)].append(s)
        return anagramDict.values()
        
