class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let res = {};
        for(let s of strs) {
            let count = new Array(26).fill(0);

            for(let c of s) {
                count[c.charCodeAt(0) - ('a').charCodeAt(0)] += 1;
            }
            count = count.join(',');
            if(res[count])
                res[count].push(s);
            else
                res[count] = [s];
        }
        
        return Object.values(res);
    }
}

/*
[] = a - z
map = {} key 
*/