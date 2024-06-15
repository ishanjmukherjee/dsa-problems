# Heap sort
# O(n log n) time complexity, where 
# n : number of elements in nums

from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create dictionary of elements in nums associated with occurrence counts
        numsDict = {}
        for num in nums:
            numsDict[num] = numsDict.get(num, 0) + 1
        
        # heapsort
        kHeap = nlargest(k, numsDict, key=numsDict.get)
        return list(kHeap)

# Reimplementing official solution
# Bucket sort
# O(n) time complexity, where
# n : number of elements in nums

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create dict where keys are numbers in nums, and values are their 
        # occurrence counts
        numsCount = {}
        for num in nums:
            numsCount[num] = numsCount.get(num, 0) + 1
        
        # bucket
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in numsCount.items():
            freq[c].append(n)
        
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
