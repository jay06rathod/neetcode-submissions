class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        pre = 1
        post = 1

        # prefix
        for i in range(n):
            res[i] = pre
            pre *= nums[i]

        # postfix
        for i in range(n-1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res