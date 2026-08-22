class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in d:
                    d[s[i]] += 1
                else:
                    d[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in d:
                d[t[i]] -= 1
        
        for val in d.values():
            if val != 0:
                return False
        
        return True