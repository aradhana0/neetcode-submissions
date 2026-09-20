class Solution {
    public int maxProduct(int[] nums) {
        int pos = 1;
        int all = 1;
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            pos = Math.max(num, pos*num);
            all *= num;
            if (all > pos) {
                pos = all;
                all = num;
            }
            max = Math.max(max, pos);
            if (all == 0) all = 1;
            if (pos == 0) pos = 1;
        }
        return max;
    }
}
