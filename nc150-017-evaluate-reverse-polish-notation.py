# My solution after reading the RPN Wikipedia
# https://en.wikipedia.org/wiki/Reverse_Polish_notation
# O(n) time complexity, where
# n : length of tokens

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalStack = []
        for c in tokens:
            if c not in "+-*/": # c is an integer
                evalStack.append(int(c))
                continue
            
            # c is an operation
            rOperand = evalStack.pop()
            lOperand = evalStack.pop()
            match c:
                case "+":
                    evalStack.append(lOperand + rOperand)
                case "-":
                    evalStack.append(lOperand - rOperand)
                case "*":
                    evalStack.append(lOperand * rOperand)
                case _: # "/"
                    evalStack.append(int(lOperand / rOperand))
                    
        return evalStack.pop()

# Reimplementing official solution
# Slight differences in writing style from my solution
# O(n) time complexity, where
# n : length of tokens

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalStack = []
        for c in tokens:
            if c == "+":
                # yay commutativity
                evalStack.append(evalStack.pop() + evalStack.pop())
            elif c == "-":
                # note the order in which tuple assignment is evaluated
                rOperand, lOperand = evalStack.pop(), evalStack.pop()
                evalStack.append(lOperand - rOperand)
            elif c == "*":
                evalStack.append(evalStack.pop() * evalStack.pop())
            elif c == "/":
                rOperand, lOperand = evalStack.pop(), evalStack.pop()
                # the integer division // operation rounds down
                # we want to truncate towards zero, so we simply chop off the
                # the decimal part
                # so, we floating divide then convert to int
                evalStack.append(int(lOperand / rOperand))
            else:
                evalStack.append(int(c))
        return evalStack.pop()

# New attempt: revisiting

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/": # is a number
                stack.append(int(token))
            elif token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                # not production quality code because it's hard to read
                # the Correct Way of Doing This is
                #   rOperand, lOperand = stack.pop(), stack.pop()
                #   stack.append(lOperand - rOperand)
                stack.append(- (stack.pop() - stack.pop()))
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            else: # token == "/"
                rOperand, lOperand = stack.pop(), stack.pop()
                stack.append(int(lOperand / rOperand))
        return stack.pop()
