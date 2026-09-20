class Solution {
    /**
     * @param {number[][]} matrix
     * @return {number[]}
     */
    spiralOrder(matrix) {
        let n = matrix.length;
        let m = matrix[0].length;
        let numOfItems = n * m;
        let spiralRes = [];
        let top=0, bottom=n-1, left = 0, right = m-1;

        while(spiralRes.length < numOfItems){
            for(let i = left; i<=right; i++){
                spiralRes.push(matrix[top][i]);
            }
            top++;

            if(spiralRes.length < numOfItems)
                for(let i = top; i<=bottom; i++){
                    spiralRes.push(matrix[i][right]);
                }
            right--;
            
            if(spiralRes.length < numOfItems)
                for(let i = right; i>=left; i--){
                    spiralRes.push(matrix[bottom][i]);     
                }
            bottom--;

            if(spiralRes.length < numOfItems)
                for(let i = bottom; i>=top; i--){
                    spiralRes.push(matrix[i][left]);
                }
            left++;
        }
        return spiralRes;
    }
}
