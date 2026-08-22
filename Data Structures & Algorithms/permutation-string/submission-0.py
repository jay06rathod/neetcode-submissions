class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        need = {}   # we have a requirement hash

        for c in s1:    # now we populate the needed characters in need hash
            need[c] = need.get(c, 0) + 1

        window = {} # we have window which traces the particular character in loop
        left = 0    
        for right in range(len(s2)):    # here is where the loop starts
            window[s2[right]] = window.get(s2[right],0) + 1 # this is where we take right in the window
            if right - left + 1 > len(s1):  # we check that after adding does the size become greater than s1
                window[s2[left]] -= 1   # if yes, remove the left most character from the window hash
                if window[s2[left]] == 0:   # if the freq of that char in window becomes 0
                    del window[s2[left]] # remove it fully making it easier to check while comparing with need
                left+=1 # then update the left
            
            if right - left + 1 == len(s1): # after all this processing we check  if the window is valid len
                if window == need:  # if yes, we check whether the window is equal to need
                    return True # if yes, return true

        return False    # or false  