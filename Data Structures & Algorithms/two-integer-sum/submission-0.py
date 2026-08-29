class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if (target - nums[i]) in seen.keys():
                return  [seen[(target - nums[i])], i] if i > seen[(target - nums[i])] else [i, seen[(target - nums[i])]]
            
            seen[nums[i]] = i
