class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        return Math.max(robHelp(nums, 0, nums.length-2), robHelp(nums, 1, nums.length-1));
    }

    private int robHelp(int[] nums, int start, int end) {
        int choice1 = 0;
        int choice2 = 0;
        while (start <= end) {
            int curr = Math.max(choice2, choice1+nums[start++]);
            choice1 = choice2;
            choice2 = curr;
        }
        System.out.println(Math.max(choice1, choice2));
        return Math.max(choice1, choice2);
    }
}
