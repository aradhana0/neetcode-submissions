class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let res = {};
        for(let i of nums) {
            if(res[i]) return true;
            res[i] = true;
        }
        return false;
    }
}
