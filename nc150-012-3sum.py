# My solution after watching up to 5:15 of the solution video 
# https://www.youtube.com/watch?v=jzZsG8n2R9A,
# i.e., up to the hint to iterate to find first number in the triplet, then 
# 2sum for target
# O(n^2) time complexity, where
# n : number of elements in nums 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i-1 >= 0:
                continue
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1          
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r:
                        l += 1
                        if nums[l] != nums[l-1]:
                            break
        return ans

# Reimplementing official solution
# O(n^2) time complexity, where
# n : number of elements in nums 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, num in enumerate(nums): # enumerate to store nums[i], missing in my 
                                       # attempt
            # small optimization missing from my attempt
            if num > 0:
                break
            
            # avoid having the same first num in triplet
            if num == nums[i-1] and i != 0:
                continue
            
            # two pointer search for 2sum
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1 # this was missing in my attempt
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans

# New attempt: revisiting

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            goal = -num
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < goal:
                    l += 1
                elif nums[l] + nums[r] > goal:
                    r -= 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # realized the problem, but didn't recall the trick 
                    # below; without this line, the test case with
                    # nums=[-2,0,0,2,2] (output should be [[-2,0,2]])
                    # fails
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans
