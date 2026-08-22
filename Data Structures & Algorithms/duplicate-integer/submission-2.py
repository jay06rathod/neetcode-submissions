class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):  # iterate the nums arr
            if nums[i] in d:    # if the number already exist in the dict
                return True # return True
            else:   # or else....
                d[nums[i]] = i  # add the count of the number (frequency of number)
        return False    # default will return False