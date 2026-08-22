class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for char in range(len(strs)):
            word = str(len(strs[char])) + '#' + strs[char]
            encoded_str += word
        return encoded_str
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = s.find('#',i)
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            res.append(word)
            i = j+1+length
        return res 
        
