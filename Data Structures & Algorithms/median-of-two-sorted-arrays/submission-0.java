class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1_len = nums1.length;
        int n2_len = nums2.length;
        int m = n1_len + n2_len;
        int[] merge = new int[m];

        System.arraycopy(nums1, 0, merge, 0, n1_len);
        System.arraycopy(nums2, 0, merge, n1_len, n2_len);
        Arrays.sort(merge);

        int mid = merge.length/2;

        if(merge.length%2!=0){
            return merge[mid];
        }
        else{
            return (merge[mid - 1] + merge[mid]) / 2.0;
        }
    }
}