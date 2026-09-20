class Solution {
    public int orangesRotting(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int[][] directions = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
        int freshCount = 0;
        for (int r=0; r<grid.length; r++) {
            for (int c=0; c<grid[0].length; c++) {
                if (grid[r][c] == 2) {
                    q.add(new int[]{r,c});
                } else if (grid[r][c] == 1) {
                    freshCount++;
                }
            }
        }
        int minutes = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            boolean fresh = false;
            while (size-- > 0) {
                int[] cell = q.poll();
                int row = cell[0];
                int col = cell[1];
                for (int[] d : directions) {
                    int r = row + d[0];
                    int c = col + d[1];
                    if (r<0 || c<0 || r>=grid.length || c>=grid[0].length || grid[r][c] == 0 || grid[r][c] == 2) continue;
                    else {
                        grid[r][c] = 2;
                        fresh = true;
                        freshCount--;
                        q.add(new int[]{r,c});
                    }
                }
            }
            if (!fresh) break;
            minutes++;
        }
        return freshCount>0 ? -1 : minutes;
    }
}
