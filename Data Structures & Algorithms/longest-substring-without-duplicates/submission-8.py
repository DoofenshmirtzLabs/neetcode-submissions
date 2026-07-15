class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #variable window size question,3 questions
        seen=set()

        max_window=0

        left=0

        for right in range(len(s)):

            while s[right] in seen:

                max_window=max(max_window,right-left)

                seen.remove(s[left])

                left+=1
            seen.add(s[right])
            right+=1
            max_window=max(max_window,right-left)
            
        return max_window