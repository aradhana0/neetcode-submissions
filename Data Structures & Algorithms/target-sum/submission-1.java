class Solution {
    int count = 0;
    public int findTargetSumWays(int[] nums, int target) {
        dfs(nums, 0, target, 0);
        return count;
    }

    private void dfs(int[] nums, int index, int target, int sum) {
        if (sum == target && index == nums.length) count++;
        if (index >= nums.length) return;
        dfs(nums, index+1, target, sum + nums[index]);
        dfs(nums, index+1, target, sum - nums[index]);
    }
}
