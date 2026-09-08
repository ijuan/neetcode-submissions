import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[right].isalnum() == False:
                right -= 1
                continue
            elif s[left].isalnum() == False:
                left += 1
                continue
            elif s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
        return True

        