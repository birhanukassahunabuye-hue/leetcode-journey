class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        win = {}
        
        formed = 0
        left = 0
        for char in t:
            need[char] = need.get(char, 0) + 1
        required = len(need)
        best_start = left
        best_length = len(s) + 1
        for right in range(len(s)):
            win[s[right]] = win.get(s[right], 0) + 1
            if s[right] in need and  win[s[right]] == need[s[right]]:
                formed +=1
           
            while formed == required:
                curr_length = right - left + 1
                if curr_length < best_length:
                     best_length = curr_length
                     best_start = left
                   
                win[s[left]] -=1
                if s[left] in need and  win[s[left]] < need[s[left]]:
                    formed -=1
                left +=1
        if best_length == len(s) + 1:
            return ""
        return s[best_start: best_start + best_length]
                
                
        