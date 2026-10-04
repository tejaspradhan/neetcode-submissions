class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal  = nums[0]
        currSum = nums[0]
        start = 0
        end = 1

        while end < len(nums):
            if currSum >=0:
                currSum+= nums[end]
            else:
                start = nums[end] 
                currSum = nums[end]
            if maxVal < currSum:
                maxVal = currSum
            end+=1
            
        return maxVal    
