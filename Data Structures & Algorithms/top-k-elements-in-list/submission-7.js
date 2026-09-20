class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let freqCounter = new Map(), res = [];
        for(let num of nums) {
            if(freqCounter.has(num)) freqCounter.set(num, freqCounter.get(num) + 1);
            else freqCounter.set(num, 1);
        }
        
        freqCounter = [...freqCounter].sort((a,b) => b[1] - a[1])


        freqCounter.forEach(n => {
            if(res.length < k)
                res.push(n[0])
           
        })
        return res.slice(0,k);
    }
}
