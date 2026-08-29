class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts = {}
        for c in s: 
            if c in char_counts.keys():
                char_counts[c]+=1
            else:
                char_counts[c]=1

        for c in t: 
            if c not in char_counts.keys():
                return False
            char_counts[c]-=1
        
        for k in char_counts.keys():
            if char_counts[k] != 0:
                return False
        return True