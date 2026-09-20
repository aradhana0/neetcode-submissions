class Solution {
    /**
     * @param {number[][]} matrix
     * @return {void}
     */
    rotate(matrix) {
        let n = matrix.length;
        if(n === 0) return matrix;
        this.transposeMatrix(matrix);
        this.reverseMatrix(matrix);
        console.log(matrix)
    }

    transposeMatrix = (matrix) => {
        let n = matrix.length;
        for(let i=0; i<n; i++){
            for(let j=i; j<n; j++){
                if(i !==j){
                    let temp = matrix[i][j];
                    matrix[i][j] = matrix[j][i];
                    matrix[j][i] = temp;
                }
            }
        }
        return matrix;
    }

    reverseMatrix = (matrix) => {
        for(let i=0; i< matrix.length; i++){
            matrix[i].reverse();
        }
    }
}
