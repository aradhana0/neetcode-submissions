class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let elMap = new Map();
    for(let i=0; i< nums.length; i++){
        if(elMap.has(nums[i])) return [elMap.get(nums[i]), i];

        elMap.set(target - nums[i], i);   
    }
    }
}
