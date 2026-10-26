class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        limit = len(nums)
        numset = set(nums)
        for i in range(1,limit+1):
            if i not in numset:
                return i
        
        return limit+1