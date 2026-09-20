class Solution {
    public int[] productExceptSelf(int[] nums) {
        //prefix product and Result array
        int[] pnr = new int[nums.length];
        pnr[0] = nums[0];
        for (int i=1; i<nums.length; i++) pnr[i] = pnr[i-1]*nums[i];
        int suffix = 1;
        for( int index = nums.length-1; index>0; index--) {
            pnr[index] = suffix * pnr[index-1];
            suffix = suffix*nums[index];
        }
        pnr[0] = suffix;
        return pnr;
    }
}  
