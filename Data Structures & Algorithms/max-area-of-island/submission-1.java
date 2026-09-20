class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int lenR = grid.length;
        int lenC = grid[0].length;
        int max = 0;
        for (int r=0; r<lenR; r++) {
            for (int c=0; c<lenC; c++) {
                if (grid[r][c] == 1) {
                    int[] res = new int[1];
                    dfs(grid, r, c, res);
                    max = Math.max(max, res[0]);
                }
            }
        }
        return max;
    }

    private void dfs(int[][] grid, int row, int col, int[] res) {
        if (row<0 || col<0 || row>=grid.length || col>=grid[0].length || grid[row][col] == 0) return;

        res[0]++;
        grid[row][col] = 0;
        dfs(grid, row+1, col, res);
        dfs(grid, row, col+1, res);
        dfs(grid, row-1, col, res);
        dfs(grid, row, col-1, res);
    }
}
