class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let n = nums.length, res = [], idx = 0;
        let freqElList= Array.from({ length: nums.length + 1 }, () => []);
        let freqCounter = {};

        for(const num of nums) {
            freqCounter[num] = (freqCounter[num] || 0) + 1;
        }

        for(const key in freqCounter) {
           freqElList[freqCounter[key]].push(key);
        }

        for(let l = n; l >= 0; l--) {
            if(freqElList[l].length > 0 && res.length < k){
                res.push(...freqElList[l])
            }
            
            if(res.length === k) return res.slice(0,k);
        }
    }
}
