class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens: 
            if t in ('+','-','*','/'):
                el1 = stack.pop()
                el2 = stack.pop()
                if t=='+':
                    stack.append(el1+el2)
                elif t=='-':
                    stack.append(el2-el1)
                elif t=='*':
                    stack.append(el1*el2)
                else:
                    stack.append(int(el2/el1))
            else:
                stack.append(int(t))
        return stack[-1]
        