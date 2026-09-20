class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length) return false;
        let sCollection = {};
        for(let str of s) {
            sCollection[str] = (sCollection[str] || 0) + 1;
        }

         for(let str of t) {
            if(!sCollection[str] || sCollection[str] === 0) return false;

            sCollection[str]--;
        }

        return true;

    }
}
