
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = ['+', '-', '*', '/']
        
        stack = []
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
                
            if char in operators:
                right = stack.pop()
                left = stack.pop()
                if char == "+":
                    result = left + right
                elif char == "-":
                    result = left - right 
                elif char  == "*":
                    result = left * right 
                elif char == "/":
                    result = int(left / right)
                
                
                stack.append(result)
        return stack[-1]
        
