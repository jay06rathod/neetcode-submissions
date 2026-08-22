class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:    # to prevent the if nums is empty
            return 0
        
        num_set = set(nums) # set which contains all the numbers 
        longest = 0 # initialized longest 

        for n in num_set:  # a loop to check before and after of n
            if n-1 not in num_set:  # here we check if the number before n exist in num_set or not, if not
                curr = n    # we make the n as current start
                count = 1   # and initialize count as 1

                while curr+1 in num_set:    # now to check number after the curr number
                    curr+=1 # if it exist simply increment curr and count
                    count+=1
                
                longest = max(longest, count)   # to compare the longest with the current count and update it with max value between them

        return longest

