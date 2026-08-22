class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # This below code snippet is the frequency map to get the number counts
        d = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        # This below code snippet is the bucket where we sort the elements based on thier frequncy using index as a frequency
        buckets = [[] for _ in range(len(nums)+1)]
        for key, val in d.items():
            buckets[val].append(key)
        
        # Choosing the kth elements
        res = []
        for b in reversed(buckets):
            res.extend(b)
        return res[:k]