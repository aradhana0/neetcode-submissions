/**
 * Pair class to store key-value pairs
 */
// class Pair {
//     /**
//      * @param {number} key The key to be stored in the pair
//      * @param {string} value The value to be stored in the pair
//      */
//     constructor(key, value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[][]}
     */
    insertionSort(pairs) {
        if(pairs.length < 1) return pairs;
        let insertionSteps = new Array();
        insertionSteps.push([...pairs]);
        for(let i=1; i<pairs.length; i++){
            let j = i-1;
            
            while(j >= 0 && pairs[j+1].key < pairs[j].key) {
                let temp = pairs[j+1];
                pairs[j+1] = pairs[j];
                pairs[j] = temp;
                j--;
            }
            insertionSteps.push([...pairs]);
        }
        return insertionSteps;
    }
}

/**
 * Dry run
 * 5,3,2,4,1
 * 3,5,2,4,1
 * 3,2,5,4,1
 * 
 */