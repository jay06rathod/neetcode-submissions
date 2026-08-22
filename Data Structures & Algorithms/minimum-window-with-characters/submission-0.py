class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}

        # put all the character that we need in the 'need' hash map
        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1

        have = 0
        needCount = len(need)

        left = 0
        mini = float("inf")
        start = 0

        # Then we put all the character in the s to window
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            # we edit if the ch is in need and whether we have allr satisfied that particular char
            if ch in need and window[ch] == need[ch]:
                have += 1  # if yes, increment have indicating we have satisfied one character
            # if we find the valid window
            while have == needCount:
                currLen = right - left + 1  # we take that valid window's len
                if currLen < mini:  # Check if it is smaller than mini
                    mini = currLen  # if yes, update the mini
                    start = left  # and keep track of start
                window[s[left]] -= (
                    1  # if we breakout of if statement, that means we can remove the left char
                )
                # if removing left affected our have == needCount thing
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1  # we change the have
                left += 1  # if it doesn't affect, we increment left

        if mini == float("inf"):  # if we have no valid window
            return ""  # We return empty string

        return s[
            start : start + mini
        ]  # if we have a valid string, return that particular substring as answer
