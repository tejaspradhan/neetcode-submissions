class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        aMax = 0
        while left < right:
            currArea = (right-left) * min(height[left], height[right])
            aMax = max(aMax, currArea)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return aMax
        