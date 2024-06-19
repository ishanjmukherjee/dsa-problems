# Reimplementing "official solution" using verbal explanation in video
# https://www.youtube.com/watch?v=ZI2z5pq0TqA
# O(n) space complexity and O(n) time complexity, where
# n : length of height

class Solution:
    def trap(self, height: List[int]) -> int:
        # create separate arrays noting max height of bars to the left & right
        # respectively
        lenHeight = len(height)
        leftMaxs = [0] * lenHeight
        rightMaxs = [0] * lenHeight
        for i in range(1, lenHeight):
            leftMaxs[i] = max(leftMaxs[i-1], height[i-1])
        for i in range(lenHeight - 2, -1, -1):
            rightMaxs[i] = max(rightMaxs[i+1], height[i+1])
        
        area = 0
        for i, h in enumerate(height):
            area += max(min(leftMaxs[i], rightMaxs[i]) - h, 0)
        return area
