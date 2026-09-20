class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);
        int[] suffixDP = new int[nums.length];
        suffixDP[nums.length-1] = nums[nums.length-1];
        suffixDP[nums.length-2] = nums[nums.length-2];
        for (int i=nums.length-3; i>=0; i--) {
            suffixDP[i] = Math.max(suffixDP[i+1], nums[i]+suffixDP[i+2]);
        }
        return suffixDP[0];
    }
}
