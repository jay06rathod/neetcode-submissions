class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        maxFreq = 0
        freq = {}
        ans = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1  # we get the right if it exist and inc
            maxFreq = max(maxFreq, freq[s[right]])  # we recompute max freq everytime

            while(right-left+1) - maxFreq > k:  # we calculate the valid window
                freq[s[left]] -= 1  # if invalid we remove the left
                left+=1  # and increment the left
            
            ans = max(ans, right-left+1)    # we recompute the max window size
        
        return ans