class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for x in nums:
            if x in freq.keys():
                freq[x]+=1
            else: 
                freq[x]=1

        while (len(result) < k):
            print( len(result), k)
            maxVal=0
            maxKey=-1
            for x in freq.keys():
                if freq[x] > maxVal and x not in result:
                    maxVal = freq[x]
                    maxKey = x 
            result.append(maxKey)
        return result

        


        