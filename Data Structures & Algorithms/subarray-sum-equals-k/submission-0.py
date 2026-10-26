class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        count = 0
        freq = {0:1}

        for num in nums:
            total += num

            if total  - k in freq:
                count += freq[total - k]
            
            freq[total] = freq.get(total, 0) + 1

        return count