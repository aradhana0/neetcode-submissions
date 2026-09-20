class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let res = [], count = new Map();
        for(let n of nums) {
            count.has(n) ? count.set(n, count.get(n) + 1) : count.set(n, 1);
            // count[n] = (count[n] || 0) + 1;
            //  if(res[count[n]]) {
            //     if(count[n])
            //         res[count[n]]
            // }
        }
        count = [...count].sort((a,b) => b[1] - a[1]);
        count.forEach(n => {
            if(k > 0) {
                res.push(n[0]);
                k--;
            }
        })
        console.log(count,res);

        return res;
    }
}
