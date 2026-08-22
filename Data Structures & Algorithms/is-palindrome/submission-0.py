class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ""


        for i in range(len(s)):
            if s[i].isalnum():
                clean_text+=s[i].lower()

        n = len(clean_text)
        l = 0 
        r = n-1
        
        while l<r:
            if clean_text[l] != clean_text[r]:
                return False
            l+=1
            r-=1

        return True