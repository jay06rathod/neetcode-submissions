class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        freq = {}
        lim = len(nums)//3
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            if freq[nums[i]] > lim:
                if nums[i] not in res:
                    res.append(nums[i])
        
        return res