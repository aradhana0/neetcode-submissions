class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int local = 0;
        for (int num : nums) {
            local = Math.max(local+num, num);
            max = Math.max(max, local);
        }
        return max;
    }
}
