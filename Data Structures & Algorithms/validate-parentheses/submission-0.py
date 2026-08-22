class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in range(len(s)):
            if s[i] in "({[":
                st.append(s[i])
            else:
                if not st:
                    return False

                if s[i] == "]":
                    if st[-1] == "[":
                        st.pop()
                    else:
                        return False
                if s[i] == ")":
                    if st[-1] == "(":
                        st.pop()
                    else:
                        return False
                if s[i] == "}":
                    if st[-1] == "{":
                        st.pop()
                    else:
                        return False
        if len(st) != 0:
                    return False
        return True