class Solution {
    public int uniquePaths(int m, int n) {
        int[][] count = new int[m+1][n+1];
        count[1][0] = 1;
        for(int r=1; r<=m; r++) {
            for (int c=1; c<=n; c++) {
                count[r][c] = count[r-1][c] + count[r][c-1];
            }
        }
        return count[m][n];
    }
}
