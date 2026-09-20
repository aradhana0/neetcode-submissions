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
            
            // if(res.length === k) return res.slice(0,k);
        }
        console.log(res.slice(0,k));
        // return res.slice(0,k);
        // return res;
        // let res = new Map(),reader = 0, counter = 0, writer = 0; 

        // while(reader <= n) {
        //     // counter = 1;
        //     if(nums[reader] !== nums[writer]){
        //         res.set(counter, nums[writer]);
        //         counter = 1;
        //         writer++;
        //         reader++;
        //     }
        //     else {
        //         counter++;
        //         reader++;
        //     }
         
        // console.log(res);
        // }
        // let idx = 0;
        // for(let l = n; l >= 1; l--) {
        //     if(res.has(l) && idx < k){
        //         freqElList.push(res.get(l));
        //         idx++;
        //     }
        //     if(idx === k) return freqElList;
        // }

        return res;
    }
}
