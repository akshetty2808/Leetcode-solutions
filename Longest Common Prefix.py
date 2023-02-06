class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        if(n == 0):
            return ""
        
        if(n == 1):
            return strs[0]

        strs.sort()

        f = len(strs[0])
        l = len(strs[n-1])
        last = min(f, l)

        i = 0
        while(i < last and strs[0][i] == strs[n - 1][i]):
            i += 1
        
        prefix = strs[0][0:i]

        return prefix