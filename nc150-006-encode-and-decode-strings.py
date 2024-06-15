# Reimplementing official solution
# Fewer assignments in decode at the cost of some readability

class Solution:

    # I don't use 
    #   for s in strs:
    #       res += str(len(s)) + "#" + s
    # because string concatenation is O(n+m) in the lengths n and m of the strings
    # to be concatenated, so repeated concatenation is O(n^2)
    # see https://stackoverflow.com/questions/37133547/time-complexity-of-string-concatenation-in-python
    def encode(self, strs: List[str]) -> str:
        strs = [str(len(s)) + "#" + s for s in strs]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i != len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordLen = int(s[i:j])
            i = j+1+wordLen
            ans.append(s[j+1:i])
        return ans
