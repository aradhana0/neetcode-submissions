class Solution {
    public int climbStairs(int n) {
        int step1 = 1;
        int step2 = 2;
        int result = n;
        while (n-- > 2) {
            result = step1+step2;
            step1 = step2;
            step2 = result;
        }
        return result;
    }
}
