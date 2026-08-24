from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = defaultdict(list)
        s_sort = tuple(sorted(s))
        t_sort = tuple(sorted(t))
        
        anagram[s_sort] = s
        anagram[t_sort] = t

        if len(anagram) == 2:
            return False
        else:
            return True
