class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        buckets = [[] for i in range(len(nums)+1)]
        # O(n)
        for x in nums:
            if x in freq.keys():
                freq[x]+=1
            else: 
                freq[x]=1

        for x in freq.keys():
            print(x, freq[x])
            buckets[freq[x]].append(x)

        index = len(buckets)-1
        while(len(result) <k):
            result.extend(buckets[index])
            index-=1

        
        
        return result[:k+1]

        


        