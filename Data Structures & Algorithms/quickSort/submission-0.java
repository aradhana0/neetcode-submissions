// Definition for a pair.
// class Pair {
//     int key;
//     String value;
//
//     public Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    public List<Pair> quickSort(List<Pair> pairs) {
        if (pairs == null || pairs.size() <=1) return pairs;
        qshelp(pairs, 0, pairs.size()-1);
        return pairs;
    }

    private void qshelp(List<Pair> pairs, int i, int j){
        if (i >= j || i<0 || i >= pairs.size() || j<0 || j>=pairs.size()) return;
        int index = i;
        int start = i;
        int pivot = j;
        int val = pairs.get(pivot).key;
        while (i < j) {
            if (pairs.get(i).key<val) {
                Pair temp = pairs.get(index);
                pairs.set(index, pairs.get(i));
                pairs.set(i, temp);
                index++;
            }
            i++;
        }
        Pair temp = pairs.get(index);
        pairs.set(index, pairs.get(pivot));
        pairs.set(pivot, temp);
        qshelp(pairs, start, index-1);
        qshelp(pairs, index+1, j);
    }
}
