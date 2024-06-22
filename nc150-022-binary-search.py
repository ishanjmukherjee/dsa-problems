# My solution
# O(n) time complexity (as specified in problem description), where
# n : length of nums

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            midIdx = i + (j - i) // 2
            midVal = nums[midIdx]
            if midVal < target:
                i = midIdx + 1
            elif midVal > target:
                j = midIdx
            else:
                return midIdx
        return -1
