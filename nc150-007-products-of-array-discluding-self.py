# Brute force
# O(n^2) time compelexity, where
# n : number of elements in nums 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j != i:
                    prod *= nums[j]
            ans[i] = prod
        return ans

# Compute product without zeros and divide by nums[i], handling edge cases
# O(n) time complexity, where
# n : number of elements in nums

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize product of all nums expect zeros
        prodWithoutZeros = 1

        # initialize number of elements which are zero
        zeroIndicesCount = 0 

        # iterate through nums to compute product without zeros and count indices
        # whose values equal zero        
        for i in range(len(nums)):
            if nums[i] != 0:
                prodWithoutZeros *= nums[i]
            else:
                zeroIndicesCount += 1
        
        if zeroIndicesCount > 1:
            return [0] * len(nums)
        elif zeroIndicesCount == 1:
            return [0 if nums[i] != 0 else prodWithoutZeros for i in range(len(nums))]
        else:
            return [prodWithoutZeros // nums[i] if nums[i] != 0 else prodWithoutZeros for i in range(len(nums))]

# Reimplementing official solution
# Iterate through nums forward then backward
# O(n) time complexity, where
# n : number of elements in nums

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        return ans
