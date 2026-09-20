class Solution {
    public boolean canPartition(int[] nums) {
        Arrays.sort(nums);
        int sum = 0;
        for(int num : nums) sum+=num;
        if (sum%2 == 1) return false;
        return dfs(nums, sum/2, 0);
    }

    private boolean dfs(int[] nums, int target, int index) {
        if (target == 0) return true;
        if (target < 0) return false;
        boolean b = false;
        for (int i=index; i<nums.length; i++) {
            b = dfs(nums, target-nums[i], i+1);
            if (b) break;
        }
        return b;
    }
}
