class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs = {}
        for s in s1:
            if s in freqs:
                freqs[s]+=1
            else:
                freqs[s]=1
        print(freqs)
        start = 0
        end = start + len(s1) -1
        for s in s2[start:end]:
            if s in freqs:
                freqs[s]-=1

        while end < len(s2):
            if s2[end] in freqs:
                freqs[s2[end]]-=1
            print(s2[start:end+1],freqs)
            if self.checkSubs(freqs):
                return True
            if s2[start] in freqs:
                freqs[s2[start]]+=1
            start+=1
            end+=1
        return False

    def checkSubs(self,freqs: dict) -> bool:
        for k in freqs:
            if freqs[k]!=0:
                return False
        return True