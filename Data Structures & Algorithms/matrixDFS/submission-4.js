class Solution {
    /**
     * @param {number[][]} grid
     * @returns {number}
     */
    countPaths(grid) {
        let visited = Array.from({ length: grid.length }, () => new Array(grid[0].length).fill(0));


        function dfs(grid, r, c, visited) {
            const rLen = grid.length, cLen = grid[0].length;

            if(Math.min(r, c) < 0 || (r === rLen || c === cLen) 
            || visited[r][c] === 1 || grid[r][c] === 1)
            return 0;

            if(r === rLen - 1 && c === cLen - 1) return 1;

            visited[r][c] = 1;
            let count = 0;

            count += dfs(grid, r + 1, c, visited);
            count += dfs(grid, r - 1, c, visited);
            count += dfs(grid, r, c + 1, visited);
            count += dfs(grid, r, c - 1, visited);

            console.log(visited, count);
            visited[r][c] = 0;

            return count;
        }

        return dfs(grid, 0, 0, visited);
    }
}
