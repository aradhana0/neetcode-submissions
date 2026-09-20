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

        while(n > 0){
            if(n % 2 === 0){
                x = x * x;
                n = n/2;
            }
            else{
                res = res * x;
                n = n - 1;
            }
        }

        return powSign ? 1/res : res;
    }
}
