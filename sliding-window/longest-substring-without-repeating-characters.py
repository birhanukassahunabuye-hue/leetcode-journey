class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        seen = set()
        for char in s:
            while char in seen:
                seen.remove(s[left])
                left +=1

            seen.add(char)
            longest = max(longest, len(seen))
        return longest
        