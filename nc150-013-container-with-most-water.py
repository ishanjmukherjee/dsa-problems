# Brute force
# Exceeds time limit on Leetcode
# O(n^2) time complexity, where
# n : number of elements in heights

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                area = (j - i) * (min(heights[j], heights[i]))
                if area > maxArea:
                    maxArea = area
        return maxArea

# My solution after seeing the thumbnail of the solution video 
# https://www.youtube.com/watch?v=UuiTKBwPgAo
# (specifically, the image of rectangles between bars shaded led me to focus
# on incremental changes in area on moving through list)
# Same as the official solution
# O(n) time complexity, where
# n : number of elements in heights

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0 # initialized value of maxArea could be anywhere between
                    # -inf and the smallest possible maxArea, i.e., 0
        l = 0 
        r = len(heights) - 1
        while l < r:
            # update maxArea
            curArea = (r - l) * (min(heights[l], heights[r]))
            maxArea = max(maxArea, curArea)

            # move whichever height is bottlenecking, i.e., shorter
            if heights[l] <= heights[r]:
                l += 1
            else: # heights[r] < heights[l]
                r -= 1
        return maxArea
