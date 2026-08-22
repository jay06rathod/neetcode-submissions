class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sorting the nums array to apply two pointers
        l = 0   
        r = len(nums)-1
        res = []
        for i in range(len(nums)):  # this loop handles only single number
            if i>0 and nums[i] == nums[i-1]:    # This checks if the two numbers are same consecutively
                continue    # If yes, then continue
            curr = nums[i]  # took the current number
            l = i+1 # increment l just 1 step ahead of i
            while l<r:  # Applying two pointers
                sumation = curr + nums[l] + nums[r] # calculating the sum
                if sumation == 0:   # if we get a match...
                    res.append([curr, nums[l], nums[r]])    # then append it to res
                    l+=1    # increment l and...
                    r-=1    # decrement r
                    while l < r and nums[l] == nums[l-1]:   # Now we check whether two left side nums are same
                        l += 1  # if yes, increment by 1
                elif sumation < 0:  # if the summation is smaller than 0, it means sum is negative
                    l+=1    # increment l
                else:   # if the sum is greater than 0, it means the number is still positive
                    r-=1    # decrement r
            r = len(nums)-1 # after every iteration, reset r only, l is allr searched so l will not be reset
        return res    # returning the result