# Reimplementing official solution
# O(log n) time complexity (as required in problem description), where
# n : length of nums

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]: # wrapped section
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    # r = mid also works
                    r = mid - 1
            else: 
                if target < nums[mid] or target > nums[r]:
                    # r = mid also works
                    r = mid - 1 
                else:
                    l = mid + 1
        return -1
