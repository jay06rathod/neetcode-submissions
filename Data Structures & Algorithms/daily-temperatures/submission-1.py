class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st = [] # stack initialized
        res = [0] * len(temp)   # pre-filling the res with 0 until len(temp)
        for i in range(len(temp)):  #iterating through temp
            while st and temp[i] > temp[st[-1]]:    # we check: stack not being empty and the curr temp to prev
                popped = st.pop()   #if the while conditions are true it will pop the items from st
                res[popped] = i-popped  # will update the res with diff of curr temp and the popped ones
            st.append(i)    # at last if while doesn't run it appends index to st
        
        return res  # returning res