class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = list(str(x))
        if(l[::1] == l[::-1]):
            return True
        else:
            return False