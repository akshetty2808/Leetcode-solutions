class Solution(object):
    def plusOne(self, digits):
        x = ''.join(str(e) for e in digits)
        n = int(x)
        n += 1
        res = [int(a) for a in str(n)]
        return res
        """
        :type digits: List[int]
        :rtype: List[int]
        """