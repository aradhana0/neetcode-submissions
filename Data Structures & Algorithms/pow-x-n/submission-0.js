class Solution {
    /**
     * @param {number} x
     * @param {number} n
     * @return {number}
     */
    myPow(x, n) {
        let powSign = n < 0;
        let res = 1;
        if(powSign) n = n * -1;

        for(let i=0; i<n; i++){
            res = res * x;
        }

        return powSign ? 1/res : res;
    }
}
