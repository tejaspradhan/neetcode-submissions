class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperBound = 0
        for n in piles:
            if n > upperBound:
                upperBound = n
        
        left, right, answer = 1, upperBound,upperBound
        while left <=right:
            mid = (left+right)//2
            reqHours = 0
            for n in piles:
                reqHours += math.ceil(n/mid)
            print(mid, reqHours)
            if reqHours > h: 
                left = mid+1
            else:
                answer = mid
                right = mid-1
                
        
        return answer
