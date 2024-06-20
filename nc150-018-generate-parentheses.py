# My solution
# Approach: generate all possible combinations of n "("s and n ")"s.
# This will create a list 2^(2*n) long (2 options, open and closed, for each
# position).
# Then, evaluate members of this list which are valid using a stack.
# Doesn't exceed time limit on Leetcode, but beats only ~5% of submissions in
# runtime and memory
# O(2^n) time complexity (saved only because n is small), where
# n : argument 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateCombinations(n):
            def genCombsHelper(k, n):
                if k == 2*n:
                    return [""]
                combsPrev = genCombsHelper(k+1, n)
                # note on nested list comprehensions here
                # https://stackoverflow.com/questions/18072759/how-can-i-use-list-comprehensions-to-process-a-nested-list
                return [newComb for comb in combsPrev for newComb in ["(" + comb, ")" + comb]]

            return genCombsHelper(0, n)
        
        ans = []
        combinations = generateCombinations(n)
        for combination in combinations:
            openParensStack = []
            poppedFromEmptyStack = False
            for c in combination:
                if c == "(":
                    openParensStack.append(0) # exact item to push doesn't matter
                elif openParensStack: # pop only if parens to close in stack
                    openParensStack.pop()
                else:
                    poppedFromEmptyStack = True
                    break  
            # valid only if no open parens remain to close, and didn't attempt to
            # close when there was no open paren
            # if valid, add to answer list
            if not openParensStack and not poppedFromEmptyStack:
                ans.append(combination)
        return ans

# Reimplementing official solution
# O(2^n) time complexity (possibly not a tight bound), where
# n : argument

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []

        def backtrack(openN: int, closedN: int) -> None:
            if (openN == closedN == n):
                ans.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return ans
