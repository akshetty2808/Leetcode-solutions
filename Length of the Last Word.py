class Solution(object):
    def lengthOfLastWord(self, s):
        x = s.split()
        n = len(x)
        return len(x[n-1])
        """
        :type s: str
        :rtype: int
        """