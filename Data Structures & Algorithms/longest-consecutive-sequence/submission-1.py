class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        
        maxCount = 0
        for n in nums:
            if (n-1) in elements:
                continue
            count = 1
            curr = n
            while (curr+1) in elements:
                count+=1
                curr+=1
            if maxCount < count:
                maxCount = count
        
        return maxCount
        