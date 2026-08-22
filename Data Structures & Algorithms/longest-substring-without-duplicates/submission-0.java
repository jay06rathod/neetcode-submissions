class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();   // we use set to add a unique char
        int left = 0;   
        int right = 0;
        int maxLen = 0;

        while(right<s.length()){    //we check the out of bounds
            char curr = s.charAt(right);    // curr character
            if(set.contains(curr)){ // if the curr in set
                set.remove(s.charAt(left)); // remove the char from left
                left++; // increment left
            }
            else{   // or else
                set.add(curr);  // add the curr in set
                maxLen = Math.max(maxLen,right-left+1);  // and check the len
                right++;    // increment right
            }
        }
        return maxLen;  // return the max len
    }
}