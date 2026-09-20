class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int dp_1 = cost[0];
        int dp_2 = cost[1];
        for (int i=2; i<cost.length; i++) {
            int curr = cost[i] + Math.min(dp_1, dp_2);
            dp_1 = dp_2;
            dp_2 = curr;
        }
        return Math.min(dp_1, dp_2);
    }
}
