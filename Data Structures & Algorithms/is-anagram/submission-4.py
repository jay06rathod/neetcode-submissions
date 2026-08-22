class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}  # initialized a dict
        if len(s) != len(t):    # if both str don't have same length 
            return False    # return false
        else:   # or else...
            for i in range(len(s)): # iterate over s
                if s[i] in d:   # check if that char of string s is allr in dict
                    d[s[i]] += 1    # if yes, increment its val (frequency)
                else:   # else
                    d[s[i]] = 1 # initialize the count
        
        for i in range(len(t)): # now we iterate for string t
            if t[i] in d:   # if the char of string t allr in dict
                d[t[i]] -= 1    # we decrement its val
        
        for val in d.values():  # now we check whether the vals of all the keys in d are empty or not
            if val != 0:    # if any val is not null we return False
                return False
        
        return True # default we return True