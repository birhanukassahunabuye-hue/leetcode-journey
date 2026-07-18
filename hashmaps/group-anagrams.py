class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
         groups = {}
         for word in strs:
             key =  ''.join(sorted(word))
           
             if not key in groups:
                 groups[key] = [word]
             else:
                 groups[key].append(word)
         return list(groups.values())