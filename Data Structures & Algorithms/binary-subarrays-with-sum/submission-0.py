class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0

        for left in range(len(nums)):
            currSum = 0

            for right in range(left, len(nums)):
                currSum += nums[right]

                if currSum == goal:
                    count += 1
                
                if currSum > goal:
                    break
        return count