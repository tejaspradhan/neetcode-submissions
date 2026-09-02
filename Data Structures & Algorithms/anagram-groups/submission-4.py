class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            char_freqs = [0]*26
            for ch in s:
                char_freqs[ord(ch)-ord('a')]+=1
            if tuple(char_freqs) in anagrams:
                anagrams[tuple(char_freqs)].append(s)
            else:
                anagrams[tuple(char_freqs)] = [s]
        
        return [x for x in anagrams.values()]
            
        