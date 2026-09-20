class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let len = nums.length;
        let prodArr = [];
        for(let i=0; i<len; i++) {
            let mul = 1;
            for(let j = 0; j<len; j++) {
                if(j !== i)
                    mul *=nums[j];
            }
        prodArr.push(mul);
        }
    return prodArr;
    }
}
