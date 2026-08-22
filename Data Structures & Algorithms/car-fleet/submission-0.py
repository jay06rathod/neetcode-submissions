class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position,speed))   # made pos and speed pair up
        pairs.sort(reverse=True)    # sort this pairs
        st = [] #initialize the stack
        for p, s in pairs:  # iteration starts
            time = (target-p)/float(s)  # we calculate the time to reach the target
            if not st:  # if the st is not empty
                st.append(time) # it means the curr time is the first car, push it to stack
            elif time<=st[-1]:  # if the curr time is smaller than the previous time in stack, we do nothing
                pass    # it means that the curr car is faster than the previous one, it will stuck behind it
            else:   # if it is the other way around
                st.append(time) # simply append it, this is our other fleet
        return len(st)  # return the len of st        