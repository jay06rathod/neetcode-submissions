class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) # length of arr
        left, leftMax = 0, 0    # Initializing the left pointer and the max of left side
        right, rightMax = n-1, 0    # Initializing the right pointer and the max of right side
        result = 0  # initializing the result as 0

        while left<right:   # starting the two pointers
            if height[left] < height[right]:    # if the left height val is smaller than right height val then..
                leftMax = max(leftMax, height[left])    # reassign the leftMax
                result += (leftMax - height[left])  # add curr result with the previous result
                left+=1 #increment left by 1
            else: # if height[left] > height[right]
                rightMax = max(rightMax, height[right]) # reassign the rightMax
                result += (rightMax - height[right])    # add the curr result with previous result
                right-=1    #decrement right by 1

        return result   # return results