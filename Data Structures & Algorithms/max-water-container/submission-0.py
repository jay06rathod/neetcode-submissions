class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height) # intializing, don't need any explanation
        l = 0
        r = n-1
        max_height = 0
        while l<r:  # starting the two pointer loop
            mini = min(height[l],height[r]) # we take minimum between l and r height
            curr = mini*(r-l)   # we multiply height * width (r-l)
            max_height = max(curr, max_height)  # we keep track of max height
            if height[l]<height[r]: # if the left height is smaller than right height...
                l+=1    # increment l
            else:   # else
                r-=1    # decrement r
        return max_height   # return the result  