class Solution {
    public int climbStairs(int n) {
        if (n <=2 ) return n;
        int first = 1;
        int second = 2;
        int count = 2;
        int index = 3;
        while (index <= n){
            count = first + second;
            first = second;
            second = count;
            index++;
        }
        return count;
    }
}
