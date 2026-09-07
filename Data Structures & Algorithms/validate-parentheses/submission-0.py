class Solution:
    def isValid(self, s: str) -> bool:
        paren={
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack=[]
        for i in s:
            if i in paren:
                if stack and stack[-1]==paren[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False


        