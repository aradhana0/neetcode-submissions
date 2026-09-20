class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length <=1) return nums.length;
        Arrays.sort(nums);
        int max = 1;
        int count = 1;
        for (int i=1; i<nums.length; i++) {
            if (nums[i] == nums[i-1]) continue;
            count = nums[i] == nums[i-1] + 1 ? count+1 : 1;
            max = Math.max(max, count);
        }
        return max;
    }
}
