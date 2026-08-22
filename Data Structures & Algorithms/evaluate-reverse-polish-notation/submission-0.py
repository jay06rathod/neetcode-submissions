class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = [] # stack initialized
        operations = {                  # operation sequence for quick calculations
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(float(a) / b)     # added float to prevent rounding off
        }
        for i in range(len(tokens)):    # Starting the loop 
            if tokens[i] not in operations: # checking if the element is a number or not
                st.append(int(tokens[i]))   # if a number then append to stack
            else:
                if st is not None:  # checking whether the stack is empty
                    num1 = st.pop() # popping out the last two numbers
                    num2 = st.pop()
                    op = tokens[i]  # taking the current operator
                    res = operations[op](num2,num1) # doing the calculations...
                    st.append(res)  # ...and appending the answer back to the stack
        
        return st[0]    # returning the value in the stack