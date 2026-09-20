// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        List<List<Pair>> ans = new ArrayList<>();
        ans.add(new ArrayList<Pair>(pairs));
        if (pairs == null || pairs.isEmpty()) return new ArrayList<>();
        if (pairs.size() == 1) return ans;
        int i = 0;
        int j = 1;
        while(j<pairs.size()) {
            int index = i; 
            while (index>=0 && j>=0 && pairs.get(j).key < pairs.get(index).key) {
                Pair temp = pairs.get(index);
                pairs.set(index, pairs.get(j));
                pairs.set(j, temp);
                index--;
                j--;
            };
            ans.add(new ArrayList<Pair>(pairs));
            i++;
            j = i+1;
        }
        return ans;
    }
}
