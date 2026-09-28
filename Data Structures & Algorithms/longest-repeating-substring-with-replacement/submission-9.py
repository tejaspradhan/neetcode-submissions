class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        start = 0
        max_freq = 0
        longest = 0
        for end in range(len(s)):
            counts[s[end]] += 1
            max_freq = max(max_freq, counts[s[end]])
            
            while (end - start + 1) - max_freq > k:
                counts[s[start]] -= 1
                start += 1
                
            longest = max(longest, end - start + 1)
        return longest
