class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if(nums.length <2) return nums.length;
        let counter, maxCounter = 0;
        let set = new Set(nums);
        set.forEach((value) => {
            let item = value;
            counter = 1;
            if(!set.has(value - 1)){
                while(set.has(++item)){
                    counter++;
                }
                maxCounter = Math.max(maxCounter, counter);
            }
        })
        return maxCounter;
    }
}
