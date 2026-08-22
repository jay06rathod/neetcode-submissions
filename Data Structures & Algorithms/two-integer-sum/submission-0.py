class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}

        for i in range(n):
            need = target - nums[i]
            if need in d:
                return [d[need], i]
            else:
                d[nums[i]] = i
