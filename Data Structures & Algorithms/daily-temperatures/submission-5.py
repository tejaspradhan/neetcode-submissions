class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # Indices of days with unresolved warmer temperatures

        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                previous_day = stack.pop()
                result[previous_day] = i - previous_day

            stack.append(i)

        return result

        