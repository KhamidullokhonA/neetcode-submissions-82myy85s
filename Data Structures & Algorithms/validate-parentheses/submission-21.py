class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', "}":"{", ']':'['}
        stack = []

        for c in s:
            if stack and c in mapping and stack[-1] == mapping[c]:
                stack.pop()
                continue
                
            stack.append(c)

        return stack == []
        
        
        