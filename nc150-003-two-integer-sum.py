# Brute force 
# O(n^2) time complexity

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # start at i + 1 to avoid returning same index twice in result list
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Create dictionary while iterating through list
# O(n) time complexity

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize dict where 
        # key   : a number in nums, and 
        # value : the number's index in nums
        numsDict = {}
        for i in range(len(nums)):
            j = numsDict.get(target - nums[i]) 
            if j == None:
                numsDict[nums[i]] = i
            else:
                # flip indices, because on first encountering a number from the 
                # pair to be returned, it is stored in the dict  
                return [j, i]

# Reimplementing official solution
# Some optimizations over my solution using dict
# O(n) time complexity

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numsDict:
                return [numsDict[complement], i]
            numsDict[num] = i

# New attempt: revisiting

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numsDict:
                return [numsDict[complement], i]
            numsDict[num] = i
