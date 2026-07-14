class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {"]":"[", ")":"(", "}":"{"}

        for c in s:

            if c in mapping and stack:
                if mapping[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
                    
                continue

                

            stack.append(c)

        return True if stack == [] else False
            

        
        