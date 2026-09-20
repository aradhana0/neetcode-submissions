class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        int col = matrix[0].length;
        int n = row*col - 1;
        int start = 0;
        while (start<=n) {
            int mid = (start+n)/2;
            int i = mid/col;
            int j = mid%col;
            if (matrix[i][j] == target) return true;
            else if (matrix[i][j] < target) start = mid+1;
            else n = mid - 1;
        }
        return false;
    }
}
