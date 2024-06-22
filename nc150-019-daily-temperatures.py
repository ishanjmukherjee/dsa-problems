# Brute force
# Passes all tests on Neetcode but exceeds time limit on Leetcode
# O(n^2) time complexity, where
# n : length of temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
        return ans

# My solution after skimming the official solution and watching an AlgoMonster
# video on the monotonic stack data structure
# https://www.youtube.com/watch?v=Dq_ObZwTY_Q
# I use a *strictly* decreasing stack.
# O(n) time complexity, where
# n : length of temperatures 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        # strictly decreasing stack
        strictStack = [] # pair: [temp, index]
        for i in range(len(temperatures) - 1, -1, -1):
            while strictStack and temperatures[i] >= strictStack[-1][0]:
                strictStack.pop()
            if strictStack:
                ans[i] = strictStack[-1][1] - i
            strictStack.append([temperatures[i], i])
        return ans

# Reimplementing official solution after verbal explanation (up to 9:24) in
# https://www.youtube.com/watch?v=cTBiBSnjO3c
# Uses less memory than official solution code because stack doesn't store 
# temperatures, only indices
# O(n) time complexity, where
# n : length of temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # store indices 
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stackIdx = stack.pop()
                ans[stackIdx] = i - stackIdx
            stack.append(i)
        return ans
