class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size=0
        left=0
        char_map={}
        for right in range(len(s)):
            if s[right] in char_map:
                left=max(char_map[s[right]]+1,left)
            char_map[s[right]]=right
            max_size=max(max_size,right-left+1)
        return max_size
        