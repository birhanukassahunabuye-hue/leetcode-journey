class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        need = {}
        win = {}
        win_length = len(s1)
        for char in s1:
            need[char] = need.get(char, 0) + 1
        
        for char in s2[:win_length]:
            win[char] = win.get(char, 0) + 1
        if win == need:
            return True
        for right in range(win_length, len(s2)):
            
                win[s2[right - win_length]]  -=1
                if win[s2[right - win_length]] == 0:
                    del win[s2[right - win_length]]
                win[s2[right]] = win.get(s2[right], 0) + 1

                if win == need:
                    return True

        return False
