class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        dict = {'(':')', '[':']', '{':'}'}
        l = []
        for i in s:
            if i in dict.keys():
                l.append(i)
            else:
                if l == []:
                    return False
                a = l.pop()
                if i != dict[a]:
                    return False
        return l == [] 
                    