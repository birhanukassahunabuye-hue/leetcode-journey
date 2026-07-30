class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ']':'[',
            '}': '{', 
            ')':'('
        }
        for char in s:

            if char in pairs.values():
                stack.append(char)
            elif char in pairs.keys():
                if not stack:
                    return False
                if pairs[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        else:
            return False