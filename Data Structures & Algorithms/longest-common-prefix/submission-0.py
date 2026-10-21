class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        i = 0
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        while strs and all(i < len(s) for s in strs):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return pref
            pref+= strs[0][i]
            i+=1
        return pref