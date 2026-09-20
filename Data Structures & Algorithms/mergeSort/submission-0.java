// Definition for a pair.
// class Pair {
//     public int key;
//     public String value;
//
//     public Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    public List<Pair> mergeSort(List<Pair> pairs) {
        if (pairs.isEmpty() || pairs.size() == 1) return pairs;
        int i = 0;
        int j = pairs.size()-1;
        return mergeSort(pairs, i, j);
    }

    private List<Pair> mergeSort(List<Pair> pairs, int i, int j) {
        if (j-i+1 <=1) return new ArrayList<>(List.of(pairs.get(i)));
        int mid = (i+j)/2;
        List<Pair> list1 = mergeSort(pairs, i, mid);
        List<Pair> list2 = mergeSort(pairs, mid+1, j);
        return mergeList(list1, list2);
    }

    private List<Pair> mergeList(List<Pair> l1, List<Pair> l2) {
        List<Pair> res = new ArrayList<>();
        int i = 0, j = 0;
        while (i<l1.size() && j<l2.size()) {
            if (l1.get(i).key<=l2.get(j).key) res.add(l1.get(i++));
            else res.add(l2.get(j++));
        }
        if (i >= l1.size()) {
            l1 = l2;
            i = j;
        }
        while (i<l1.size()) res.add(l1.get(i++));
        return res;
    }
}
