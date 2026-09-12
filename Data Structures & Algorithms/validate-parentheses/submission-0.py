class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()

        for ch in s:
            if ch in ('[','{','('):
                d.append(ch)
            elif len(d) > 0:
                removed = d.pop()
                if (ch ==']' and removed !='[') or (ch =='}' and removed !='{') or (ch ==')' and removed !='('):
                    return False
            else:
                return False
            
        
        if len(d)!=0:
            return False
        
        return True

