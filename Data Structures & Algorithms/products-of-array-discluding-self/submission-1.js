class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let len = nums.length;
        let prodArr = [];
        let prefMul = [1], suffMul = [1];
        for(let i=1; i<len; i++) {
            prefMul.push((prefMul[i-1] ?? 1) * nums[i-1]);
        }
        for(let j=len-2; j >=0; j--) {
            suffMul.push((suffMul[len - j - 2]) * nums[j+1]);
        }
        console.log(prefMul, suffMul)
        for(let i=0; i<len; i++) {
            prodArr.push(prefMul[i] * suffMul[len - i - 1]);
        }
    
    return prodArr;
    }
}
