class Solution {
    public int countPaths(int[][] grid) {
        Set<String> seen = new HashSet<>();
        return helper(grid, 0, 0, seen);
    }

    private int helper(int[][] grid, int row, int col, Set<String> seen) {
        int lenR = grid.length;
        int lenC = grid[0].length;
        if (row<0 || col<0 || row>=lenR || col>=lenC) return 0;
        String node = row + "," + col;
        if (seen.contains(node) || grid[row][col] == 1) return 0;
        if (row == lenR-1 && col == lenC-1 && grid[row][col] == 0) return 1;
        seen.add(node);
        int count = helper(grid, row+1, col, seen) +
            helper(grid, row, col+1, seen) +
            helper(grid, row-1, col, seen) +
            helper(grid, row, col-1, seen);
        seen.remove(node);
        return count;
    }
}
