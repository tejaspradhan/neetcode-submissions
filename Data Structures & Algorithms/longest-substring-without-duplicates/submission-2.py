class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        maxLen = 0
        positions = {}
        while end < len(s):
            if s[end] in positions:
                start = max(positions[s[end]]+1,start)
            positions[s[end]] = end
            maxLen = max(maxLen , end - start +1)
            end+=1
        return maxLen