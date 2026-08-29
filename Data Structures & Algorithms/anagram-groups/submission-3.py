class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            char_counts = [0]*26
            for c in s:
                char_counts[ord(c) - ord('a')]+=1
            if tuple(char_counts) in  anagrams.keys():
                anagrams[tuple(char_counts)].append(s)
            else:
                anagrams[tuple(char_counts)] = [s]
        
        return [el for el in anagrams.values()]