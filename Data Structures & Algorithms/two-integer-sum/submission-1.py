class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)   # count length of array nums
        d = {}  # initialize dictionary

        for i in range(n):  # iterate over array nums
            need = target - nums[i] # we subtract in order to know the diff
            if need in d:   # if we get the diff
                return [d[need], i] # we return the curr i and the need
            else:   # else
                d[nums[i]] = i  # simply add that number with its index
