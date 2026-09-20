class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        for(let i =0; i<nums.length; i++) {
            for(let j=i + 1; j < nums.length; j++) {
                if(nums[i] + nums[j] === target) return [i, j];
                
            }
        }
    }
}

/*
4 5 6
6 t = 6
5

*/
