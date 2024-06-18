# Keep a stack of open parens
# O(n) time complexity, where
# n : length of string

class Solution:
    def isValid(self, s: str) -> bool:
        def complement(c: chr) -> chr:
            if c == '(':
                return ')'
            if c == '{':
                return '}'
            return ']'

        
        openParens = []
        for c in s:
            if c in "({[":
                openParens.append(c)
            else:
                # popping from empty list is invalid, but if list is empty,
                # len(openParens) == 0 evaluates to true and short-circuiting
                # in boolean evaluation means the second condition doesn't get
                # evaluated.                
                if len(openParens) == 0 or c != complement(openParens.pop()):
                    return False
        return len(openParens) == 0

# Reimplementing official solution
# Adding quirks like using a map instead of a complement function and using
#   not stack
# instead of 
#   len(stack) == 0
# Interestingly, this takes more time on Leetcode than the solution using a 
# complement function. My guess is this is because setting up a dict is 
# time-taking and overkill when you have just 3 keys -- you can just linear 
# search.
# O(n) time complexity, where
# n : length of string

class Solution:
    def isValid(self, s: str) -> bool:
        openToClosed = {'(': ')', '{': '}', '[': ']'}
        openParens = []
        for c in s:
            if c in openToClosed:
                openParens.append(c)
            else:
                # popping from empty list is invalid, but if list is empty,
                # len(openParens) == 0 evaluates to true and short-circuiting
                # in boolean evaluation means the second condition doesn't get
                # evaluated.                
                if not openParens or c != openToClosed[openParens.pop()]:
                    return False
        return not openParens  
