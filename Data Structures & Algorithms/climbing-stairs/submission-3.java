class Solution {
    public int climbStairs(int n) {
        int step1 = 1;
        int step2 = 2;
        int count = n;
        int index = 3;
        while (index <= n){
            count = step1 + step2;
            step1 = step2;
            step2 = count;
            index++;
        }
        return count;
    }
}
