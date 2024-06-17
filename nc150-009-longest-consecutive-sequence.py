# Reimplementing official solution
# O(n) time complexity, where
# n : length of list nums

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in numsSet:
            if num - 1 not in numsSet:
                length = 1
                while num + length in numsSet:
                    length += 1
                longest = max(longest, length)
        return longest
