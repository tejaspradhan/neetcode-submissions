class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        i = 1
        stack.append([temperatures[0],0])
        while i < len(temperatures):
            if len(stack) > 0 and temperatures[i] <= stack[-1][0]:
                stack.append([temperatures[i],i])
            else:
                while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                    el, j = stack.pop()
                    result[j] = i - j
                stack.append([temperatures[i],i])
            i+=1
        return result
            
        