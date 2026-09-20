/** Pair class to store key-value pairs */
// class Pair {
//   /**
//    * @param {number} key The key to be stored in the pair
//    * @param {string} value The value to be stored in the pair
//    */
//   constructor(key, value) {
//       this.key = key;
//       this.value = value;
//   }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[]}
     */
    mergeSort(pairs) {
        let n = pairs.length;
        if(n <= 1) return pairs;
        let l = 0, m = Math.floor(n/2), r = n-1;
        return this.mergeSorts(pairs, l, r);
        // let l = 0, m = Math.floor(n/2), r = n-1;
        // if(l < r) {
        //     this.mergeSort(pairs.slice(l, m));
        //     this.mergeSort(pairs.slice(m+1));

        //    return this.mergeLists(pairs,l,m,r);
        // }
        // return pairs;
    }
    mergeSorts(arr, l,  r) {
        if (l < r) {
            // Find the middle point of arr
            let m = Math.floor((l + r) / 2);

            this.mergeSorts(arr, l, m);   // sort left half
            this.mergeSorts(arr, m+1, r); // sort right half
            this.mergeLists(arr, l, m, r);    // merge sorted halfs
        }
        return arr;
    }
    mergeLists(arr, l, m, r) {
        // Find lengths of two subarrays to be merged
        let length1 = m - l + 1;
        let length2 = r - m;

        // Create temp arrays 
        let dummyArrLeft = new Array(length1);
        let dummyArrRight = new Array(length2);

        // Copy the sorted left & right halfs to temp arrays
        for (let i = 0; i < length1; i++) {
            dummyArrLeft[i] = arr[l + i];
        }
        
        for (let j = 0; j < length2; j++) {
            dummyArrRight[j] = arr[m + 1 + j];
        }
        // console.log(dummyArrLeft, dummyArrRight)

        let i = 0, j = 0, k = l;

        while(i < dummyArrLeft.length && j < dummyArrRight.length) {
            if(dummyArrLeft[i].key <= dummyArrRight[j].key){
                arr[k++] = dummyArrLeft[i++];
            }
            else if(dummyArrLeft[i].key > dummyArrRight[j].key){
                arr[k++] = dummyArrRight[j++];
            }
            // else {
            //     console.log(dummyArrLeft[i].value, dummyArrRight[j].value, dummyArrLeft[i].value < dummyArrRight[j].value)
            //     if(dummyArrLeft[i].value < dummyArrRight[j].value) {
            //           arr[k++] = dummyArrLeft[i++];
            //     }
            //     else{
            //         arr[k++] = dummyArrRight[j++];
            //     }
            // }
        }
        while(i < dummyArrLeft.length){
            arr[k++] = dummyArrLeft[i++]; 
        }
        while(j < dummyArrRight.length){
            arr[k++] = dummyArrRight[j++]; 
        }
        return arr;
    }
}

/**
 * Edge cases: 
 * a. length <= 1
 */