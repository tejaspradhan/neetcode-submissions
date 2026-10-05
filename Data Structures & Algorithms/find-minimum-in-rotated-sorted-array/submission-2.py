class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2
            #print(left, right,mid, nums[mid])
            if nums[mid] < nums[mid+1]:
                if nums[mid-1] < nums[mid]:
                    minVal = min(self.findMin(nums[left:mid]),self.findMin(nums[mid:right+1]))
                    return minVal
                else:
                    return nums[mid]
            else:
                return nums[mid+1]

        return nums[left]