class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)  # Setting low and high
        while low<high: # Starting a while loop 
            mid = (low+high)//2     # calculating mid 
            total = sum((pile + mid - 1) // mid for pile in piles)  # sum all the speed for every pile
            if total<=h:    # If the the total speed smaller than the hrs, it is feasible
                high = mid  # Therefore, update high to mid
            else:   # or else
                low = mid+1     # Increase the low to mid + 1
        
        return low  # Atlast return low